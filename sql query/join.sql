WITH q_period_orders AS (
  SELECT o.order_id, o.customer_id
  FROM orders o
  WHERE o.status = 'DELIVERED'
    AND o.order_date >= DATE '2025-04-01'
    AND o.order_date <  DATE '2025-07-01'
),

refund_sum AS (
  SELECT r.order_id, r.product_id, SUM(r.qty_refunded) AS qty_refunded_sum
  FROM refunds r
  GROUP BY r.order_id, r.product_id
),

promotion_value AS (
  SELECT
    ip.order_id,
    ip.product_id,
    p.promo_id,
    CASE
      WHEN p.promo_type = 'FIXED'   THEN p.discount_value
      WHEN p.promo_type = 'PERCENT' THEN NULL  
      ELSE 0
    END AS fixed_discount,
    CASE
      WHEN p.promo_type = 'PERCENT' THEN p.discount_value
      ELSE NULL
    END AS percent_discount
  FROM item_promotions ip
  JOIN promotions p ON p.promo_id = ip.promo_id
),
best_discount AS (
  SELECT
    oi.order_id,
    oi.product_id,
    MAX(
      CASE
        WHEN pv.percent_discount IS NOT NULL THEN oi.unit_price * (pv.percent_discount / 100.0)
        WHEN pv.fixed_discount   IS NOT NULL THEN pv.fixed_discount
        ELSE 0
      END
    ) AS max_discount_amount
  FROM order_items oi
  LEFT JOIN promotion_value pv
    ON pv.order_id = oi.order_id
   AND pv.product_id = oi.product_id
  GROUP BY oi.order_id, oi.product_id
),
item_revenue AS (
  SELECT
    q.order_id,
    q.customer_id,
    c.category_id,
    c.category_name,

    GREATEST(oi.qty - COALESCE(rs.qty_refunded_sum, 0), 0) AS net_qty,
    GREATEST(oi.unit_price - COALESCE(bd.max_discount_amount, 0), 0) AS effective_unit_price
  FROM q_period_orders q
  JOIN order_items oi
    ON oi.order_id = q.order_id
  JOIN products pr
    ON pr.product_id = oi.product_id
  JOIN categories c
    ON c.category_id = pr.category_id
  LEFT JOIN refund_sum rs
    ON rs.order_id = oi.order_id AND rs.product_id = oi.product_id
  LEFT JOIN best_discount bd
    ON bd.order_id = oi.order_id AND bd.product_id = oi.product_id
),

cust_cat_rev AS (
  SELECT
    customer_id,
    category_id,
    category_name,
    SUM(net_qty * effective_unit_price) AS net_revenue
  FROM item_revenue
  WHERE net_qty > 0  
  GROUP BY customer_id, category_id, category_name
),

ranked AS (
  SELECT
    customer_id,
    category_id,
    category_name,
    net_revenue,
    ROW_NUMBER() OVER (
      PARTITION BY customer_id
      ORDER BY net_revenue DESC, category_name ASC
    ) AS rn
  FROM cust_cat_rev
)
SELECT
  r.customer_id,
  r.category_name AS top_category,
  r.net_revenue  AS top_category_net_revenue
FROM ranked r
WHERE r.rn = 1
ORDER BY r.customer_id;
