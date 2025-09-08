from collections import deque
import sys
input = sys.stdin.readline

# 입력
R, C, K = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
# 벽 정보
# wall_h[x][y] = True 면 (x,y) 와 (x-1,y) 사이에 벽
# wall_v[x][y] = True 면 (x,y) 와 (x,y+1) 사이에 벽
wall_h = [[False]*C for _ in range(R)]
wall_v = [[False]*C for _ in range(R)]
for _ in range(W):
    x, y, t = map(int, input().split())
    x -= 1; y -= 1
    if t == 0:
        wall_h[x][y] = True
    else:
        wall_v[x][y] = True

# 온풍기와 조사할 칸 위치 수집
heaters = []      # (r, c, dir)
targets = []      # [(r,c), ...]
# dir: 0=오른쪽, 1=왼쪽, 2=위, 3=아래
for i in range(R):
    for j in range(C):
        if 1 <= room[i][j] <= 4:
            heaters.append((i, j, room[i][j]-1))
        elif room[i][j] == 5:
            targets.append((i,j))
# 온도 그리드 초기화
temperature = [[0]*C for _ in range(R)]

# 4방향 델타 (오른, 왼, 위, 아래)
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 온풍기 바람 확산용 델타 및 이동 시 벽 확인 체크 함수
# 각 방향마다 바람이 퍼지는 세 가지 경로 (직진 / 위·대각 / 아래·대각)
# (dir, kind) -> (delta_r, delta_c), 벽 검사 정보
spread_info = {
    0: [  # → 방향
        ((0,1),   lambda r,c: not wall_v[r][c]),
        ((-1,1),  lambda r,c: (r>0 and not wall_h[r][c] and not wall_v[r-1][c])),
        ((1,1),   lambda r,c: (r<R-1 and not wall_h[r+1][c] and not wall_v[r+1][c])),
    ],
    1: [  # ← 방향
        ((0,-1),  lambda r,c: not wall_v[r][c-1]),
        ((-1,-1), lambda r,c: (r>0 and not wall_h[r][c] and not wall_v[r-1][c-1])),
        ((1,-1),  lambda r,c: (r<R-1 and not wall_h[r+1][c] and not wall_v[r+1][c-1])),
    ],
    2: [  # ↑ 방향
        ((-1,0),  lambda r,c: not wall_h[r][c]),
        ((-1,-1), lambda r,c: (c>0 and not wall_v[r][c] and not wall_h[r][c-1])),
        ((-1,1),  lambda r,c: (c<C-1 and not wall_v[r][c+1] and not wall_h[r][c+1])),
    ],
    3: [  # ↓ 방향
        ((1,0),   lambda r,c: not wall_h[r+1][c]),
        ((1,-1),  lambda r,c: (c>0 and not wall_v[r][c] and not wall_h[r+1][c-1])),
        ((1,1),   lambda r,c: (c<C-1 and not wall_v[r][c+1] and not wall_h[r+1][c+1])),
    ],
}

def blow_from_heater():
    """모든 온풍기에서 바람 한 번 불어서 temp_add에 합산"""
    temp_add = [[0]*C for _ in range(R)]
    for hr, hc, d in heaters:
        visited = [[False]*C for _ in range(R)]
        q = deque()
        # 첫 칸 (온풍기 바로 옆) 온도 +5
        nr, nc = hr + dr[d], hc + dc[d]
        visited[nr][nc] = True
        temp_add[nr][nc] += 5
        q.append((nr,nc,5))
        # BFS: 세 가지 경로로 k-1 만큼 계속
        while q:
            r, c, k = q.popleft()
            if k == 1: continue
            for delt, can_move in spread_info[d]:
                rr, cc = r + delt[0], c + delt[1]
                # 범위 & 방문 & 벽 체크
                if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc] and can_move(r,c):
                    visited[rr][cc] = True
                    temp_add[rr][cc] += k-1
                    q.append((rr,cc,k-1))
    # 합산
    for i in range(R):
        for j in range(C):
            temperature[i][j] += temp_add[i][j]

def adjust_temperature():
    """인접 칸 온도 조절"""
    delta = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if not (0<=nr<R and 0<=nc<C): continue
                # 벽이 있으면 패스
                if d==0 and wall_v[r][c]: continue
                if d==1 and wall_v[r][c-1]: continue
                if d==2 and wall_h[r][c]: continue
                if d==3 and wall_h[r+1][c]: continue
                diff = (temperature[r][c] - temperature[nr][nc]) // 4
                if diff > 0:
                    delta[r][c] -= diff
                    delta[nr][nc] += diff
    # 한꺼번에 적용
    for i in range(R):
        for j in range(C):
            temperature[i][j] += delta[i][j]

def decrease_boundary():
    """가장자리 온도 1씩 감소"""
    for i in range(R):
        if temperature[i][0] > 0:    temperature[i][0] -= 1
        if temperature[i][C-1] > 0:  temperature[i][C-1] -= 1
    for j in range(C):
        if temperature[0][j] > 0:    temperature[0][j] -= 1
        if temperature[R-1][j] > 0:  temperature[R-1][j] -= 1

def check_targets():
    """조사 칸이 모두 K 이상인지 검사"""
    return all(temperature[r][c] >= K for r,c in targets)

# 시뮬레이션
chocolate = 0
while True:
    chocolate += 1
    # 1) 바람
    blow_from_heater()
    # 2) 온도 조절
    adjust_temperature()
    # 3) 가장자리 감소
    decrease_boundary()
    # 4) 검사
    if check_targets() or chocolate > 100:
        break

print(chocolate if chocolate <= 100 else 101)
