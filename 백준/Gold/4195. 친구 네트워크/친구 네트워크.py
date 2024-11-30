# 4195. G2 친구 네트워크
import sys
input = sys.stdin.readline

def make_set(n):
    p = list(range(n))
    net = [1]*n
    return p, net

def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parents[root_y] = root_x
        network[root_x] += network[root_y]
    print(network[root_x])

T = int(input())

for tc in range(1, T+1):
    F = int(input())
    parents, network = make_set(2*F)

    dict_p_idx = {}
    temp = 0

    for _ in range(F):
        inf = list(input().split())
        for i in range(2):
            if dict_p_idx.get(inf[i]) == None:
                dict_p_idx[inf[i]] = temp
                temp += 1
        # print(dict_p_idx)
        # 숫자로 바꿈
        union(dict_p_idx[inf[0]], dict_p_idx[inf[1]])
        # print(parents)