# 1865. 웜홀
import sys
input = sys.stdin.readline

def bellman_ford(start):

    dist = [10001]*(N+1)
    dist[start] = 0

    for _ in range(N-1):
        for i in range(1, len(edge)):
            u, v, w = edge[i][0], edge[i][1], edge[i][2]
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    for i in range(1, len(edge)):
        u, v, w = edge[i][0], edge[i][1], edge[i][2]
        if dist[v] > dist[u] + w:
            return -1

    return 1


T = int(input())
for tc in range(1, T+1):
    # N: 지점수, M: 도로의 개수, W:웜홀의 개수
    N, M, W = map(int, input().split())
    edge = [()]  # [(), (1,2,3), (2,3,4), (3,1,-8)]]

    # 도로정보 M개
    for _ in range(M):
        # S, E : 연결된 지점의 번호, T: 이 도로를 통해 이동하는데 걸리는 시간
        S, E, T = map(int, input().split())
        edge.append((S, E, T))
        edge.append((E, S, T))

    # 웜홀 정보 W개
    for _ in range(W):
        # S: 시작 지점, E: 도착 지점, T: 줄어드는 시간
        S, E, T = map(int, input().split())
        edge.append((S, E, -T))

    result = bellman_ford(1)

    if result == -1:
        print('YES')
    else:
        print('NO')