# 1520 내리막길 G3
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def DFS(cx, cy):

    if cx==M-1 and cy==N-1:
        return 1

    if visited[cx][cy] != -1:
        return visited[cx][cy]

    visited[cx][cy] = 0

    for k in range(4):
        nx = cx + dx[k]
        ny = cy + dy[k]

        if nx<0 or nx>= M or ny<0 or ny>=N:
            continue

        if world_map[cx][cy] <= world_map[nx][ny]:
            continue

        visited[cx][cy] += DFS(nx, ny)

    return visited[cx][cy]

# M은 세로 N은 가로
M, N = map(int, input().split())
world_map = [list(map(int, input().split())) for _ in range(M)]
visited = [[-1]*N for _ in range(M)]

print(DFS(0, 0))