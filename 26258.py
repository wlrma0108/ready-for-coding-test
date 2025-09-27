import sys
import bisect as b

def sc(s):
    n = s[0] == '-'
    if n: s = s[1:]
    if '.' in s:
        a, c = s.split('.', 1)
        c = c[:1] if c else '0'
        v = int(a) * 10 + int(c)
    else:
        v = int(s) * 10
    return -v if n else v

r = sys.stdin.buffer.readline
n = int(r())
xs = [0]*n
ys = [0]*n
xs10 = [0]*n
for i in range(n):
    a, b_ = r().split()
    xi = int(a); yi = int(b_)
    xs[i] = xi; ys[i] = yi; xs10[i] = xi*10

sg = [0]*(n-1)
for i in range(n-1):
    d = ys[i+1] - ys[i]
    sg[i] = 1 if d > 0 else (-1 if d < 0 else 0)

q = int(r())
o = []
for _ in range(q):
    k = r().strip().decode()
    k10 = sc(k)
    j = b.bisect_left(xs10, k10)
    o.append(str(sg[j-1]))

print("\n".join(o))
