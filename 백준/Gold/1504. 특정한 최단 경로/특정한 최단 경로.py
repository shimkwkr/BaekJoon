# 1504 특별한 최단 경로

# 1753. 최단 경로

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start):

    min_heap = [(0, start)]

    dist = [float('inf')] * (V+1)
    dist[start] = 0

    while min_heap:
        cost, node = heappop(min_heap)

        if dist[node] < cost:
            continue

        for nxt_node, nxt_weight in adj[node]:
            if dist[nxt_node] > cost + nxt_weight:
                dist[nxt_node] = cost + nxt_weight
                heappush(min_heap, (dist[nxt_node], nxt_node))

    return dist

V, E = map(int ,input().split())

adj = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

v1, v2 = map(int, input().split())

dist_1_to_N = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

if min(dist_1_to_N[v1] + dist_v1[v2] + dist_v2[V], dist_1_to_N[v2] + dist_v2[v1] + dist_v1[V]) == float('inf'):
    print(-1)
else:
    print(min(dist_1_to_N[v1] + dist_v1[v2] + dist_v2[V], dist_1_to_N[v2] + dist_v2[v1] + dist_v1[V]))
