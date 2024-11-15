# 16987 G5 계란으로 계란치기

def DFS(eggs, start):

    if start == N:
        cnt = 0
        for i in range(N):
            if is_break[i]:
                cnt += 1

        result.append(cnt)
        return

    # start의 계란이 깨져있다면
    if is_break[start]:
        DFS(eggs, start+1)
        return

    for i in range(N):
        if start == i:
            continue

        if is_break[i]:
            continue

        eggs[start][0] -= eggs[i][1]
        eggs[i][0] -= eggs[start][1]
        if eggs[start][0] <= 0 :
            is_break[start] = True
        if eggs[i][0] <= 0:
            is_break[i] = True

        DFS(eggs, start+1)

        eggs[start][0] += eggs[i][1]
        eggs[i][0] += eggs[start][1]
        if eggs[start][0] > 0 :
            is_break[start] = False
        if eggs[i][0] > 0:
            is_break[i] = False

    cnt = 0
    for i in range(N):
        if is_break[i]:
            cnt += 1
    result.append(cnt)



N = int(input())

Eggs = []
# S 내구도, W 무게
for _ in range(N):
    S, W = map(int, input().split())
    Eggs.append([S, W])

result = []
is_break = [False]*N
start_egg = 0
DFS(Eggs, start_egg)

if len(result) >0:
    print(max(result))
else:
    print(0)
