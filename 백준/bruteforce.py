N = 10  # 노드 개수 예시(작게 잡음)
K = 3   # K진 트리


parent = [0] * (N+1)
parent[1] = 0  
for i in range(2, N+1):
    parent[i] = (i-2)//K + 1

print("각 노드의 부모:", parent)

def get_path_to_root(x, parent):
    path = []
    while x != 0:
        path.append(x)
        x = parent[x]
    return path  # (자기자신~루트)
    
def get_parent(node, K):
    if K == 1:
        return node - 1
    else:
        return (node - 2) // K + 1 if node != 1 else 1

def brute_force_distance(x, y, K):
    cnt = 0
    while x != y:
        if x > y:
            x = get_parent(x, K)
        else:
            y = get_parent(y, K)
        cnt += 1
    return cnt

# 사용 예시:
N, K, Q = 9, 3, 3  # 입력 예시
queries = [(8, 9), (5, 7), (8, 4)]

for x, y in queries:
    if K == 1:
        print(abs(x - y))
    else:
        print(brute_force_distance(x, y, K))
