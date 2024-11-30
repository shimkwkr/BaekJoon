# 17141 연구소 2

import copy
# import sys
# sys.stdin = open('lab_2.txt')

# 바이러스가 발생할수 있는 좌표의 조합
def nCr(ans, n, r):

    if r == len(ans):
        min_time_virus(ans)
        return

    if n == len(can_virus):
        return

    ans.append(can_virus[n])
    nCr(ans, n+1, r)
    ans.pop()
    nCr(ans, n+1, r)

def min_time_virus(ans):
    global min_time
    global can_or_cant

    temp_can_virus = copy.deepcopy(ans)
    temp_lab = copy.deepcopy(lab)
    temp_visited = copy.deepcopy(visited)
    temp_time = 0
    cnt = 0

    for x,y in temp_can_virus:
        temp_lab[x][y] = 0
        temp_visited[x][y] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while len(temp_can_virus) > 0:
        temp_time += 1
        q_size = len(temp_can_virus)
        for _ in range(q_size):
            cx, cy = temp_can_virus.pop(0)

            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]

                if nx<0 or nx>=N or ny<0 or ny>=N or temp_lab[nx][ny] != 0 or temp_visited[nx][ny] != 0:
                    continue

                temp_can_virus.append((nx, ny))
                temp_visited[nx][ny] = 1
                temp_lab[nx][ny] = temp_time

        # for i in temp_lab:
        #     print(*i)
        # print('----------------------------')
    temp_time -= 1

    for i in range(N):
        for j in range(N):
            if temp_lab[i][j] == 0:
                cnt += 1

    if cnt == M:
        can_or_cant = 1
        if min_time > temp_time:
            min_time = temp_time


N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
can_virus = []
min_time = 99999999
can_or_cant = 0

# 바이러스를 놓을수 있는 위치를 저장
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            can_virus.append((i, j))
            lab[i][j] = 0

        if lab[i][j] == 1:
            lab[i][j] = '-'
            visited[i][j] = 1

# 바이러스가 발생할수 있는 좌표의 조합
nCr([], 0, M)

if can_or_cant == 1:
    print(min_time)
else:
    print(-1)


