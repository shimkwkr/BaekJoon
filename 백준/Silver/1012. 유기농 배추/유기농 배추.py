# 1012. S2 유기농 배추
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(i, j, arr, visited):
    if arr[i][j] == 0:
        return

    if visited[i][j]:
        return

    visited[i][j] = True

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if ni>=0 and ni<M and nj>=0 and nj<N:
            DFS(ni, nj, arr, visited)


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int ,input().split())

    arr = [[0] * N  for _ in range(M)]
    visited = [[False] * N  for _ in range(M)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1

    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1 and not visited[i][j]:
                cnt += 1
                DFS(i, j, arr, visited)

    print(cnt)
