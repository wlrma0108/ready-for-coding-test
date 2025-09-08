import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())

def parent(x):
    if x == 1:
        return 1
    return (x - 2) // K + 1

if K == 1:
  
    for _ in range(Q):
        x, y = map(int, input().split())
        print(abs(x - y))
else:
    for _ in range(Q):
        x, y = map(int, input().split())
        cnt = 0
        while x != y:
            if x > y:
                x = parent(x)
            else:
                y = parent(y)
            cnt += 1
        print(cnt)
