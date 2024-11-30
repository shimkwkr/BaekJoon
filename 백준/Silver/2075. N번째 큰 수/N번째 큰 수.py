import heapq

n=int(input())
heap=[]
for _ in range(n):
    l=list(map(int,input().split()))
    
    for x in l:
        if len(heap)<n:
            heapq.heappush(heap, x)
        else:
            t=heapq.heappop(heap)
            if t<x:
                heapq.heappush (heap, x)
            else:
                heapq.heappush(heap, t)
print (heapq.heappop(heap))