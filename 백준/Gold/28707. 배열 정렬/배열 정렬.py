# 28707. G1 배열 정렬
from heapq import heappop, heappush

def dijkstra(A, edges):
    dist = dict()
    visited = dict()
    A = tuple(A)
    hq = [(0, A)]
    dist[A] = 0

    while hq:
        weight, node = heappop(hq)

        if visited.get(node) is not None:
            continue

        visited[node] = True

        for u, v, w in edges:
            temp = list(node)
            next_weight = weight + w
            temp[u-1], temp[v-1] = temp[v-1], temp[u-1]

            temp = tuple(temp)

            if dist.get(temp) is None:
                dist[temp] = next_weight
                heappush(hq, (next_weight, temp))

            else:
                if dist[temp] > next_weight:
                    dist[temp] = next_weight
                    heappush(hq, (next_weight, temp))
    return dist


N = int(input())
A = list(map(int, input().split()))
M = int(input())
edges = [list(map(int, input().split())) for _ in range(M)]

target = tuple(sorted(A))

DIST = dijkstra(A, edges)

if DIST.get(target) is None:
    print(-1)
else:
    print(DIST[target])