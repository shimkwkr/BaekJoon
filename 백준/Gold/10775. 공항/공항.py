# 10775 G2 공항
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def make_set():
    p = list(range(G+1))
    return p

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

G = int(input())
P = int(input())
cnt = 0

parents = make_set()

for _ in range(P):
    gi = int(input())
    find_root = find_set(gi)
    if find_root == gi:
        parents[gi] -= 1
        cnt += 1
    elif find_root != gi:
        if find_root == 0:
            print(cnt)
            exit()
        else:
            parents[find_root] -= 1
            cnt += 1
print(cnt)
