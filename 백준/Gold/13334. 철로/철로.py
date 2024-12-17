# 13334 G2 철로

from heapq import heappop, heappush
import sys
input = sys.stdin.readline


n = int(input())

arr = []

for _ in range(n):
    start, end = map(int, input().split())
    if start > end:
        start, end = end, start

    heappush(arr, (end, start))

d = int(input())


possible = []
cnt = 0
ans = 0

while arr:
    end, start = heappop(arr)

    if start >= end-d:
        heappush(possible, (start, end))
        cnt += 1

    while possible:
        s, e = heappop(possible)

        if s >= end-d:
            heappush(possible, (s, e))
            break
        else:
            cnt -=1

    ans = max(ans, cnt)

print(ans)