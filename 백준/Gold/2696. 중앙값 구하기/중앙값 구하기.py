# 2696. G2 중앙값 구하기

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    M = int(input())
    cnt_enter = M//10 + 1
    stop = 0
    arr = []

    while stop < cnt_enter:
        temp = list(input().split())
        for i in range(len(temp)):
            arr.append(temp[i])
        stop += 1

    left_heap = []
    right_heap = []
    answer = []

    for i in range(len(arr)):

        if len(left_heap) == len(right_heap):
            heappush(left_heap, -int(arr[i]))
        else:
            heappush(right_heap, int(arr[i]))

        if right_heap and right_heap[0] < -left_heap[0]:
            left_value = heappop(left_heap)
            right_value = heappop(right_heap)

            heappush(left_heap, -right_value)
            heappush(right_heap, -left_value)

        if i % 2 == 0:
            answer.append(-left_heap[0])

    print(len(answer))

    for i in range(len(answer)//10+1):
        if i == len(answer)//10:
            print(*answer[i*10:])
        else:
            print(*answer[i*10:i*10+10])
