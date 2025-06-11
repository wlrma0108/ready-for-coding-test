N = 10  # 노드 개수 예시(작게 잡음)
K = 3   # K진 트리


parent = [0] * (N+1)
parent[1] = 0  
for i in range(2, N+1):
    parent[i] = (i-2)//K + 1

print("각 노드의 부모:", parent)