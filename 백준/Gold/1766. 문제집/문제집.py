# 1766. G2 문제집
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int ,input().split())
adj = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

hq = []
result = []

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    indegree[v] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        heappush(hq, i)

while hq:
    now = heappop(hq)
    result.append(now)

    for i in adj[now]:
        indegree[i]-=1
        if indegree[i]==0:
            heappush(hq, i)

print(*result)