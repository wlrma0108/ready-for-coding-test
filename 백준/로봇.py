import sys
from collections import deque

input = sys.stdin.readline
# 못풀어서 gpt사용
# BFS로 (sx,sy)에서 맵 전체에 대한 최단거리를 구해서 dist_map[y][x]에 저장
def bfs(sx, sy, w, h, grid):
    dist = [[-1]*w for _ in range(h)]
    q = deque()
    q.append((sx, sy))
    dist[sy][sx] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < w and 0 <= ny < h:
                if grid[ny][nx] != 'x' and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((nx, ny))
    return dist

def solve():
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        grid = [list(input().rstrip('\n')) for _ in range(h)]

        # 1) 시작 위치와 더러운 칸 좌표 모으기
        points = []  # (x,y) 리스트. 인덱스 0은 로봇 시작, 그 뒤는 더러운 칸
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 'o':
                    points.insert(0, (x,y))
                elif grid[y][x] == '*':
                    points.append((x,y))

        d = len(points) - 1  # 더러운 칸 개수
        # 2) 각 점마다 BFS로 다른 점들까지의 거리를 구해 dist_matrix에 저장
        dist_matrix = [[0]*(d+1) for _ in range(d+1)]
        for i, (x, y) in enumerate(points):
            dist_map = bfs(x, y, w, h, grid)
            for j, (xx, yy) in enumerate(points):
                dist_matrix[i][j] = dist_map[yy][xx]

        # 3) 어떤 더러운 칸이라도 도달 불가(-1)이면 답은 -1
        unreachable = any(dist_matrix[i][j] == -1 for i in range(d+1) for j in range(d+1))
        if unreachable:
            print(-1)
            continue

        # 4) DP 비트마스크로 TSP: dp[i][mask] = 시작점→방문한 더러운 칸 집합=mask, 현재 i에 있을 때 최소 이동 횟수
        INF = 10**9
        # mask는 0..(1<<d)-1. bit k (0<=k<d)가 켜져 있으면 더러운 칸 k(=points[k+1]) 방문 완료.
        dp = [[INF]*(1<<d) for _ in range(d+1)]
        dp[0][0] = 0

        for mask in range(1<<d):
            for u in range(d+1):
                if dp[u][mask] == INF: 
                    continue
                # 아직 방문하지 않은 더러운 칸 v를 다음에 방문
                for k in range(d):
                    if not (mask & (1<<k)):
                        v = k + 1
                        next_mask = mask | (1<<k)
                        new_cost = dp[u][mask] + dist_matrix[u][v]
                        if new_cost < dp[v][next_mask]:
                            dp[v][next_mask] = new_cost

        full_mask = (1<<d) - 1
        ans = min(dp[i][full_mask] for i in range(1, d+1)) if d > 0 else 0
        print(ans)

if __name__ == '__main__':
    solve()