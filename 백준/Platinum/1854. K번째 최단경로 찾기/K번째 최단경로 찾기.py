# 1854 P4. K번째 최단 경로 찾기
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start):
    pq = [(0, start)]

    dist = [[] for _ in range(n + 1)]
    heappush(dist[start], 0)

    while pq:
        weight, node = heappop(pq)

        for nxt_weight, nxt_node in adj[node]:
            new_weight = weight + nxt_weight

            if len(dist[nxt_node]) < m:
                heappush(dist[nxt_node], -new_weight)
                heappush(pq, (new_weight, nxt_node))
            elif new_weight < -dist[nxt_node][0]:
                heappop(dist[nxt_node])
                heappush(dist[nxt_node], -new_weight)
                heappush(pq, (new_weight, nxt_node))

    for i in range(1, n+1):
        if len(dist[i]) < m:
            print(-1)
        else:
            print(-dist[i][0])

n, k, m = map(int ,input().split())

adj = [[] for _ in range(n+1)]

for _ in range(k):
    u, v ,w = map(int, input().split())

    adj[u].append((w, v))


start_node = 1
dijkstra(start_node)
