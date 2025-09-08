import sys                                   # 표준 입력을 빠르게 읽기 위해 sys 모듈 사용
from collections import deque                # BFS 구현에 사용할 deque(양쪽 끝 큐)



def main():                                  # 반복 입력에서 속도 향상을 위해 readline 별칭 지정
    input = sys.stdin.readline
    N, M, V = map(int, input().split())      # N: 정점 수, M: 간선 수, V: 시작 정점

    adj = [[] for _ in range(N + 1)]         # 1번부터 N번까지 쓰기 위해 N+1 길이의 인접 리스트 준비
    for _ in range(M):                       # M개의 간선을 입력받아
        a, b = map(int, input().split())     # 무방향 간선 (a - b)
        adj[a].append(b)                      # a의 이웃에 b를 추가
        adj[b].append(a)                      # b의 이웃에 a를 추가 (무방향이므로 양쪽에 모두 추가)

    for i in range(1, N + 1):                # "작은 번호 먼저 방문" 규칙을 위해
        adj[i].sort()                         # 각 정점의 인접 정점 목록을 오름차순으로 정렬

    # -------------------------
    # DFS (반복: 스택 사용)
    # -------------------------
    dfs_order = []                            # DFS 방문 순서를 담을 리스트
    visited = [False] * (N + 1)               # 방문 여부 배열 (1..N)

    stack = [V]                               # DFS는 스택에 시작 정점 V를 넣고 시작
    while stack:                              # 스택이 빌 때까지 반복
        v = stack.pop()                       # 스택의 맨 위(최근)에 넣은 정점을 꺼냄
        if visited[v]:                        # 이미 방문했다면
            continue                          # 스킵하고 다음 루프로
        visited[v] = True                     # 처음 방문 처리
        dfs_order.append(v)                   # 방문 순서에 v를 기록

        # 주의: 스택은 LIFO이므로 "작은 번호 먼저 꺼내지려면"
        # 인접 정점을 역순으로 푸시해야 함 (adj[v]는 오름차순 정렬되어 있음)
        for nv in reversed(adj[v]):           # v에 인접한 정점들을 큰 것부터 스택에 넣기
            if not visited[nv]:               # 아직 방문 전인 경우에만
                stack.append(nv)              # 스택에 push (나중에 pop되어 방문)

    # -------------------------
    # BFS (큐 사용)
    # -------------------------
    bfs_order = []                            # BFS 방문 순서를 담을 리스트
    visited = [False] * (N + 1)               # 방문 여부 배열을 DFS와 독립적으로 다시 초기화

    q = deque([V])                            # 큐에 시작 정점 V를 넣고 시작
    visited[V] = True                         # 큐에 넣을 때 바로 방문 처리(중복 삽입 방지)
    while q:                                  # 큐가 빌 때까지 반복
        v = q.popleft()                       # 큐의 맨 앞에서 하나 꺼냄 (FIFO)
        bfs_order.append(v)                   # 방문 순서에 v 기록
        for nv in adj[v]:                     # v의 인접 정점들을 "작은 번호부터" 확인 (이미 정렬됨)
            if not visited[nv]:               # 아직 방문하지 않은 정점이면
                visited[nv] = True            # 큐에 넣는 시점에 방문 처리
                q.append(nv)                  # 큐에 삽입 (나중에 순서대로 꺼내 방문)

    # -------------------------
    # 출력 (요구 형식)
    # -------------------------
    print(" ".join(map(str, dfs_order)))      # 첫 줄: DFS 결과 (V부터 방문된 순서)
    print(" ".join(map(str, bfs_order)))      # 둘째 줄: BFS 결과 (V부터 방문된 순서)

if __name__ == "__main__":                    # 모듈로 임포트될 때 실행되지 않도록 가드
    main()