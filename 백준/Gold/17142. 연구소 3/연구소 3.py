# 17142. 연구소 3

from collections import deque

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
    
    # list slicing으로 깊은 복사를 해주었다
    lab_temp = [lab[i][:] for i in range(N)]
    visited_temp = [visited[i][:] for i in range(N)]

    # can_virus_temp 는 queue 이므로 deque로 선언
    can_virus_temp = deque()

    cnt = 0
    temp_time = 0

    temp_min_time = 0

    for i in range(len(ans)):
        can_virus_temp.append(ans[i][:])
        # 이번에 생성된 바이러스 시작 좌표는 0으로 만들어줌
        lab_temp[ans[i][0]][ans[i][1]] = 0
        # 이번에 생성된 바이러스 시작 좌표의 visited는 1로 만들어줌
        visited_temp[ans[i][0]][ans[i][1]] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while len(can_virus_temp) > 0:
        temp_time += 1
        q_size = len(can_virus_temp)
        for _ in range(q_size):
            cx, cy= can_virus_temp.popleft()

            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]

                if nx<0 or nx>=N or ny<0 or ny>=N or visited_temp[nx][ny] != 0:
                    continue

                # 1-1 다음 지역이 안전지역이 아니라면
                if lab_temp[nx][ny] != 0:
                    # 2-1만약 다음 지역이 비활성화 바이러스라면
                    if lab_temp[nx][ny] == '*':
                        visited_temp[nx][ny] = 1
                        can_virus_temp.append((nx, ny))
                        lab_temp[nx][ny] = 0

                    # 2-2그외에 다른 0이 아닌 숫자거나 벽이라면
                    else:
                        continue
                
                # 1-2 다음 지역이 안전지역이라면
                else:
                    visited_temp[nx][ny] = 1
                    can_virus_temp.append((nx, ny))
                    lab_temp[nx][ny] = temp_time

        
    temp_time -= 1

    for i in range(N):
        for j in range(N):
            if lab_temp[i][j] == 0:
                cnt += 1
            elif lab_temp[i][j] == '*':
                cnt += 1
            if lab_temp[i][j] not in ['-', '*']:
                if temp_min_time < lab_temp[i][j]:
                    temp_min_time = lab_temp[i][j]
    
    
    if cnt == len(can_virus):
        can_or_cant = 1
        if min_time > temp_min_time:
            min_time = temp_min_time
                    
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
can_virus = []
min_time = 99999999
can_or_cant = 0

for i in range(N):
    for j in range(N):
        # 벽을 찾으면
        if lab[i][j] == 1:
            lab[i][j] = '-'
            visited[i][j] = 1
        # 바이러스를 놓을수 있는곳을 찾으면
        if lab[i][j] == 2:
            lab[i][j] = '*'
            can_virus.append((i, j))

nCr([], 0, M)
            
if can_or_cant == 0:
    print(-1)
else:
    print(min_time)

