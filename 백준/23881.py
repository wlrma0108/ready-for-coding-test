import sys

r = sys.stdin.readline

n, k = map(int, r().split())
a = list(map(int, r().split()))

cnt = 0  

for last in range(n - 1, 0, -1):
    mx_idx = 0
    mx_val = a[0]
    ##print("mx for문 시작")
    for j in range(1, last + 1):
        ##print("sucess1")
        if a[j] > mx_val:
            mx_val = a[j]
            mx_idx = j

    if mx_idx != last:
        x, y = a[mx_idx], a[last]  
        a[mx_idx], a[last] = a[last], a[mx_idx]
        cnt += 1
        ##print("sucess2")
        if cnt == k:
            if x < y:
                print(x, y)
            else:
                print(y, x)
            sys.exit(0)


print(-1)