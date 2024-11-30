

import sys
input = sys.stdin.readline

INF = int(1e9)

def bf(start, end):
    dist = [-INF] * (n+1)
    dist[start] = 0
    # 현재노드(index)기준 바로 직전 노드를 저장하는 노드
    route= [0] * (n+1)
    result = []

    # 원래는 n-1 이지만 마지막 번쨰에는 음의사이클에 속한 녀석들은
    # 다 INF로 할당해줄거다
    for i in range(n):
        for u, v , w in edges[1:]:
            if dist[u] == -INF:
                continue

            if dist[v] < dist[u] + w:
                dist[v] = dist[u] + w
                # 직전 노드가 어디인지 저장
                route[v] = u

                # 마지막 for룹은 음의 사이클인지 아닌지 확인
                # 음의 사이클에 포함된 녀석들은 INF로 할당해준다
                if i == n-1:
                    dist[v] = INF

    # 도착지가 음의 사이클에 포함되어있는지 확인
    if dist[end] == INF:
        print(-1)
        return

    # 아무런 문제가 없다면
    result.append(end)
    while end != start:
        result.append(route[end])
        end = route[end]

    result.reverse()
    print(*result)

n, m = map(int, input().split())
edges = [[]]

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])

start_vertex = 1
bf(start_vertex, n)