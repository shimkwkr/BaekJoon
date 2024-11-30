# 4386 G3 별자리만들기
import sys
from math import sqrt

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def make_set():
    p = list(range(n+1))
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

def kruskal(edges, n):
    cnt = 0
    mst = []

    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u, v)
            cnt += 1
            mst.append(w)
            if cnt == n-1:
                break
    return mst

n = int(input())
p = make_set()
star_pos_idx = {}
stars = []
cnt = 1
edges = []
parents = make_set()

for _ in range(n):
    star_inf = tuple(map(float, input().split()))
    stars.append(star_inf[:])
    star_pos_idx[star_inf] = cnt
    cnt += 1

for i in range(n-1):
    for j in range(i+1, n):
        w = sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
        edges.append((star_pos_idx[stars[i]], star_pos_idx[stars[j]], w))

edges.sort(key=lambda x : x[2])

MST = kruskal(edges, n)

print(round(sum(MST),2))
