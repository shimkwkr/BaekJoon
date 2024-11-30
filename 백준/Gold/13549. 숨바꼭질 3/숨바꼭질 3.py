# 13549 숨바꼭질3 G5
import sys

input = sys.stdin.readline
from collections import deque


def bfs():
    q = deque()
    cnt = 0
    # visited에 현재 idx에 도달하기 까지의 시간을 저장
    visited = [-1] * 100001

    if N == 0:
        q.append(N)
        visited[0] = 0
    else:
        temp = N
        while temp <= 100000:
            q.append(temp)
            visited[temp] = 0

            temp *= 2

    while q:
        q_size = len(q)
        for _ in range(q_size):
            node = q.popleft()

            if node == K:
                print(visited[K])
                return

            for i in [node + 1, node - 1]:
                if i < 0:
                    continue
                j = i
                if j > 0:
                    while j <= 100000:
                        if visited[j] == -1 or visited[j] == visited[node] + 1:
                            q.append(j)
                            visited[j] = visited[node] + 1
                        j *= 2
                elif j == 0:
                    if visited[j] == -1 or visited[j] == visited[node] + 1:
                        q.append(j)
                        visited[j] = visited[node] + 1


N, K = map(int, input().split())
bfs()