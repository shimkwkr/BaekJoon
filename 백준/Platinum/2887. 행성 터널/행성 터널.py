# 2887 P5 행성 터널
import sys
input = sys.stdin.readline

def make_set():
    p = list(range(N))
    return p

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parents[root_y] = root_x

def kruskal(edges, N):
    cnt = 0
    mst = 0

    for inf in edges:
        if find_set(inf[0]) != find_set(inf[1]):
            union(inf[0], inf[1])
            cnt = 0
            mst += inf[2]
    return mst

N = int(input())
parents = make_set()
x_list, y_list, z_list = [], [], []
edges = []

for i in range(N):
    x, y, z = map(int, input().split())
    x_list.append((x, i))
    y_list.append( (y, i) )
    z_list.append( (z, i) )

x_list.sort()
y_list.sort()
z_list.sort()

for col_list in [x_list, y_list, z_list]:
    for i in range(1, N):
        w_a, idx_a = col_list[i]
        w_b, idx_b = col_list[i-1]
        edges.append( (idx_a, idx_b, abs(w_a-w_b)) )

edges.sort(key = lambda x : x[2])
MST = kruskal(edges, N)

print(MST)
