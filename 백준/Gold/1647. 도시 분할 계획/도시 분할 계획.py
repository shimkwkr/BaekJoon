# 1647. G4 도시 분할 계획
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def make_set():
    p = list(range(N+1))
    return p

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    parents[root_y] = root_x

def kruskal(edges, N):
    cnt = 0
    mst = []

    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u, v)
            mst.append(w)
            cnt += 1
            if cnt == N-1:
                break
    return mst

N, M = map(int ,input().split())
parents = make_set()
edges = []

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

edges.sort(key = lambda x : x[2])

MST = kruskal(edges, N)

print(sum(MST[:-1]))