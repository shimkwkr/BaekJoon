from collections import deque

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

queue = deque()

#초기 익은 토마토의 위치를 저장
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i,j))
            visited[i][j] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

time = 0

while len(queue)>0:
    # 현재 토마토
    q_size = len(queue)
    
    for _ in range(q_size):

        cx, cy= queue.popleft()
        
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
        
            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] == 1 or box[nx][ny] != 0:
                continue

            box[nx][ny] = 1
            visited[nx][ny] = 1
            queue.append((nx, ny))

    time += 1
time -= 1

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()

print(time)