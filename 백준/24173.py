import sys
input = sys.stdin.readline

cnt = 0
K = 0
ans_small = -1
ans_large = -1
found = False

def swap_and_count(A, i, j):
    global cnt, K, ans_small, ans_large, found
    x, y = A[i], A[j]
    A[i], A[j] = A[j], A[i]
    cnt += 1
    if cnt == K:
        if x < y:
            ans_small, ans_large = x, y
        else:
            ans_small, ans_large = y, x
        found = True

def heapify(A, k, n):
    if found:
        return
    left = 2 * k
    right = left + 1

    if right <= n:
        if A[left] < A[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return

    if A[smaller] < A[k]:
        swap_and_count(A, k, smaller)
        if found:
            return
        heapify(A, smaller, n)

def build_min_heap(A, n):
    for i in range(n // 2, 0, -1):
        if found:
            return
        heapify(A, i, n)

def heap_sort(A, n):
    build_min_heap(A, n)
    if found:
        return
    for i in range(n, 1, -1):
        swap_and_count(A, 1, i)  
        if found:
            return
        heapify(A, 1, i - 1)
        if found:
            return

def main():
    global K, found, ans_small, ans_large
    N, K = map(int, input().split())
    arr = [0] + list(map(int, input().split()))  

    heap_sort(arr, N)

    if found:
        print(ans_small, ans_large)
    else:
        print(-1)

if __name__ == "__main__":
    main()
