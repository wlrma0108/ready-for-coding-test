import heapq

def main():
    N = int(input())  
    left_heap = []  
    right_heap = []  
    
    for _ in range(N):
        num = int(input())  
        
        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, -num)  
        else:
            heapq.heappush(right_heap, num)  
            
        if right_heap and -left_heap[0] > right_heap[0]:  
            left_top = -heapq.heappop(left_heap)
            right_top = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -right_top)
            heapq.heappush(right_heap, left_top)
        
        print(-left_heap[0])  
