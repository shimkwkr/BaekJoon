# 14503 로봇 청소기 G5
import sys
input = sys.stdin.readline

# 초기 방향
dir_dict = {0:3, 1:2, 2:1, 3:0}

# 서 남 동 북
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def clean(cx, cy, dir):
    cnt = 0
    temp = False

    while True:
        # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
        if visited[cx][cy] == 0:
            cnt += 1
            visited[cx][cy] = 2

        # 4방향 탐색
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]

            # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
            if visited[nx][ny] == 0:
                # 90도 반시계 방향 회전
                dir = (dir+1)%4
                # 바라보는 뱡향 이 청소되지 않은 빈칸인 경우 전진
                if visited[cx + dx[dir]][cy + dy[dir]] == 0:
                    cx, cy = cx + dx[dir], cy + dy[dir]
                temp = True
                break
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        if temp:
            temp = False
            continue

        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        cx, cy = cx-dx[dir], cy-dy[dir]
        # 만약 후진한곳이 벽이라면
        if visited[cx][cy] == 1:
            return cnt


# 방의 크기 N, M
N, M = map(int, input().split())
# 처음 로봇 청소기의 칸 좌표 (r, c), 바라보는 방향 d
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        # 벽은 visited 1로 설정
        if room[i][j] == 1:
            visited[i][j] = 1

print(clean(r, c, dir_dict[d]))



