# 1219. 오민식의 고민
import sys

input = sys.stdin.readline
from collections import deque

# INF 상수 설정
INF = -int(1e9)


def bf(s, e):
    dist = [INF] * N
    dist[s] = money[s]

    for _ in range(N - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[v] < dist[u] + w:
                dist[v] = dist[u] + w

    if dist[e] == INF:
        return 'gg'

    for u, v, w in edges:
        # 음의 사이클이 발견되었을때
        if dist[u] != INF and dist[v] < dist[u] + w:
            # 만약 사이클이 있음에도 목적지에 도착할 수 있을때
            if bfs(v, e):
                return 'Gee'
            # 만약 사이클이 있지만 목적지에 도착할 수 없을때
            else:
                pass

    return dist[e]


def bfs(start, end):
    q = deque()
    q.append(start)

    visited = [False] * N
    visited[start] = True

    while q:
        now = q.popleft()

        if now == end:
            return True

        for u, v, w in edges:
            if now == u:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
    return False


# N: 도시의 수, S: 시작 도시, E: 도착 도시, M: 교통 수단의 개수
N, S, E, M = map(int, input().split())
edges = []

for _ in range(M):
    start_city, end_city, cost = map(int, input().split())
    edges.append([start_city, end_city, -cost])

money = list(map(int, input().split()))

# 도착지 기준 해당 도시의 돈을 받으므로 도착지에 따라 간선의 가중치를 재 계산해준다
for i in range(M):
    edges[i][2] = edges[i][2] + money[edges[i][1]]

# 시작 도시와 도착도시를 가지고 bellman_ford 알고리즘 시작
print(bf(S, E))
