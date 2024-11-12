# 2206 G3. 벽 부수고 이동하기
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0))
# 시작visited는 7로 잡은 왜냐? 내마음
visited[0][0] = 7
cnt = 1

if N == 1 and M == 1:
    print(1)
    exit()

while q:
    q_size = len(q)
    for _ in range(q_size):
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if nx == N-1 and ny == M-1:
                cnt += 1
                print(cnt)
                exit()

            if 0<=nx<N and 0<=ny<M:
                # 만약 이동하려는 곳이 벽이라면
                if arr[nx][ny] == 1:
                    # 아직 벽을 한번도 부수지 않았다면
                    if visited[cx][cy] == 7:
                        visited[nx][ny] = 6
                        q.append((nx, ny))
                # 만약 이동하려는 곳이 벽이 아니라면
                else:
                    # (현재 위치 visited가 7인데) 다음 이동하려는 곳의 visited가 6또는 0인 경우
                    if (visited[cx][cy] == 7 and visited[nx][ny] == 6) or (visited[cx][cy] == 7 and visited[nx][ny] == 0):
                        visited[nx][ny] = 7
                        q.append((nx, ny))
                    elif visited[cx][cy] == 6 and visited[nx][ny] == 0:
                        visited[nx][ny] = 6
                        q.append((nx, ny))

    cnt += 1
print(-1)