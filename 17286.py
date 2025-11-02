from itertools import permutations

yumi = tuple(map(int, input().split()))
peeps = [tuple(map(int, input().split())) for _ in range(3)]

def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

ans = min(dist(yumi, p[0]) + dist(p[0], p[1]) + dist(p[1], p[2]) 
          for p in permutations(peeps))

print(int(ans))