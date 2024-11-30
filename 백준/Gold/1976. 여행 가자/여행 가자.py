# 1976. G4 여행 가자
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

def union(x,y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    parents[root_y] = root_x

N = int(input())
M = int(input())

parents = make_set()

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    for j in range(1, N+1):
        if arr[j-1] == 1:
            union(i, j)

travel = list(map(int, input().split()))

root = find_set(travel[0])
for i in range(1, len(travel)):
    if find_set(travel[i]) != root:
        print('NO')
        exit()

print('YES')