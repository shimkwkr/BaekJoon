# 17471. G3 게리맨더링
from collections import deque

def combi(arr, n):
    if n == N:
        if len(arr) != N and len(arr) != 0:
            can_seperate(arr)
        return

    arr.append(zone[n])
    combi(arr, n+1)
    arr.pop()
    combi(arr, n+1)

def can_seperate(arr):
    global ans
    zone_num = [0]*(N+1)
    visited = [False]*(N+1)
    opposit_arr = list(set(zone) - set(arr))

    for i in arr:
        zone_num[i] = 1
    for i in opposit_arr:
        zone_num[i] = 2

    q1 = deque()
    q1.append(arr[0])
    visited[arr[0]] = True
    cnt_1 = 0

    while q1:
        # print(q1)
        node = q1.popleft()
        cnt_1 += population[node - 1]
        for nxt_node in adj[node]:
            if zone_num[nxt_node] == 1 and not visited[nxt_node]:
                visited[nxt_node] = True
                q1.append(nxt_node)


    q2 = deque()
    q2.append(opposit_arr[0])
    visited[opposit_arr[0]] = True
    cnt_2 = 0

    while q2:
        node = q2.popleft()
        cnt_2 += population[node - 1]
        for nxt_node in adj[node]:
            if zone_num[nxt_node] == 2 and not visited[nxt_node]:
                visited[nxt_node] = True
                q2.append(nxt_node)


    for i in range(1, N+1):
        if not visited[i]:
            return

    if ans > abs(cnt_1-cnt_2):
        ans = abs(cnt_1-cnt_2)
        # print(arr, opposit_arr, ans)



N = int(input())
population = list(map(int, input().split()))

adj = [[] for _ in range(N+1)]
for u in range(1, N+1):
    inf = list(map(int, input().split()))
    for v in inf[1:]:
        adj[u].append(v)

zone = list(range(1, N+1))
ans = float('inf')
combi([], 0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)

