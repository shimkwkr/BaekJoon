# 1202. 보석 도둑

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, K = map(int ,input().split())
jewelrys = []
bags = []

for _ in range(N):
    M, V = map(int ,input().split())
    jewelrys.append((M, V))

for _ in range(K):
    C = int(input())
    bags.append(C)

jewelrys.sort()
bags.sort()

jewel_idx = 0
possible_jewels = []
answer = 0

for bag in bags:
    while jewel_idx < N and jewelrys[jewel_idx][0] <= bag:
        heappush(possible_jewels, -jewelrys[jewel_idx][1])
        jewel_idx += 1

    if possible_jewels:
        answer -= heappop(possible_jewels)

print(answer)

