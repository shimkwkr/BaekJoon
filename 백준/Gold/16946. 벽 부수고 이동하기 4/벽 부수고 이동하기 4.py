# 16946. G2. 벽 부수고 이동하기 4
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check_zero():
    zero_Zones = {}
    zone_id = 2

    def BFS(x, y):
        zone_size = 1
        arr[x][y] = str(zone_id)

        q = deque()
        q.append((x, y))

        while q:
            cx, cy = q.popleft()

            for k in range(4):
                nx, ny = cx + dx[k], cy + dy[k]

                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] == '0':
                        arr[nx][ny] = str(zone_id)
                        q.append((nx, ny))
                        zone_size += 1

        return str(zone_size % 10)

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '0':
                zone_size = BFS(i, j)
                zero_Zones[str(zone_id)] = zone_size
                zone_id += 1

    return zero_Zones


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
result = [['0']*M for _ in range(N)]

zero_Zones = check_zero()

for i in range(N):
    for j in range(M):
        total = 1
        if arr[i][j] == '1':
            can_move = set()
            for k in range(4):
                ni, nj = i+dx[k], j + dy[k]

                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] != '1':
                        can_move.add(arr[ni][nj])

            for num in can_move:
                total += int(zero_Zones[num])
            result[i][j] = str(total % 10)

for i in result:
    print(''.join(i))