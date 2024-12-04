# 11779 G3 최소비용 구하기2

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(adj, start):
    dist = [float('inf')]*(n+1)
    dist[start] = 0
    visited = [False]*(n+1)
    pq = [(0, start)]
    course = [[] for _ in range(n+1)]
    course[start] = [start]

    while pq:
        weight, node = heappop(pq)

        if visited[node]:
            continue

        visited[node] = True
        for nxt_weight, nxt_node in adj[node]:
            if not visited[nxt_node]:
                if dist[nxt_node] > dist[node] + nxt_weight:
                    dist[nxt_node] = dist[node] + nxt_weight
                    heappush(pq, (dist[nxt_node], nxt_node))
                    course[nxt_node] = course[node][:]
                    course[nxt_node].append(nxt_node)
    return dist, course

n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]

for i in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

start, end = map(int, input().split())

Dist, Course = dijkstra(adj, start)
print(Dist[end])
print(len(Course[end]))
print(*Course[end])

