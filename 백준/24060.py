import sys
input = sys.stdin.readline

cnt = 0        
K = 0          
ans = -1       
found = False  
tmp = []       

def merge(A, p, q, r):
    global cnt, K, ans, found, tmp
    i = p
    j = q + 1
    t = 1

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1; i += 1
        else:
            tmp[t] = A[j]
            t += 1; j += 1

    # 왼쪽 남은 거
    while i <= q:
        tmp[t] = A[i]
        t += 1; i += 1

    # 오른쪽 
    while j <= r:
        tmp[t] = A[j]
        t += 1; j += 1

    i = p
    t = 1
    while i <= r:
        A[i] = tmp[t]
        cnt += 1
        if cnt == K:
            ans = A[i]
            found = True
            return    
        i += 1
        t += 1

def merge_sort(A, p, r):
    if found:
        return
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        if found:
            return
        merge_sort(A, q + 1, r)
        if found:
            return
        merge(A, p, q, r)

def main():
    global K, tmp, found, ans
    N, K = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    tmp = [0] * (N + 1)                         

    merge_sort(arr, 1, N)

    if found:
        print(ans)
    else:
        print(-1)

if __name__ == "__main__":
    main()
