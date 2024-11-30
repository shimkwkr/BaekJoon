# 1043 G4 거짓말
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

    if root_x in know_true and root_y in know_true:
        return
    elif root_x in know_true:
        parents[root_y] = root_x
    elif root_y in know_true:
        parents[root_x] = root_y
    else:
        parents[root_y] = root_x

N, M = map(int, input().split())
know_true = list(map(int, input().split()))[1:]
exaggrated = [0]*(N+1)
# 부모 배열 선언
parents = make_set()
# 과장된 말을 할 수 있는 파티의 개수
cnt = 0
parties = []

for i in range(M):
    party_inf = list(map(int, input().split()))

    for j in range(1, party_inf[0]):
        union(party_inf[j], party_inf[j+1])

    parties.append(party_inf[1:])

for party in parties:
    for i in party:
        if find_set(i) in know_true:
            break
    else:
        cnt += 1

print(cnt)