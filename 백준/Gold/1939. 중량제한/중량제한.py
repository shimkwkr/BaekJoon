# 1939. G3 중량제한
import sys
from collections import deque
input = sys.stdin.readline

def bfs(target):
    visited[S] = True
    q = deque()
    q.append(S)

    while q:
        now = q.popleft()
        if now == E:
            return True
        for nx, nw in adj[now]:
            if not visited[nx] and nw >= target:
                q.append(nx)
                visited[nx] = True

    return False

# N개의 섬, M개의 다리
N, M = map(int, input().split())

# 인접리스트
adj = [[] for _ in range(N+1)]

for i in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

S, E = map(int ,input().split())

start, end = 1, 1000000000
ans = 0
while start <= end:
    visited = [False]*(N+1)
    mid = (start + end) // 2
    if bfs(mid):
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)