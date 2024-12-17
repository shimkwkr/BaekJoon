# 1655. G2 가운데를 말해요

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
left_heap = []
right_heap = []

for _ in range(N):
    num = int(input())
    if len(left_heap) == len(right_heap):
        heappush(left_heap, -num)
    else:
        heappush(right_heap, num)

    if right_heap and right_heap[0] < -left_heap[0]:
        left_value = heappop(left_heap)
        right_value = heappop(right_heap)
        heappush(right_heap, -left_value)
        heappush(left_heap, -right_value)

    print(-left_heap[0])
