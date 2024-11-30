from collections import deque

# 먹이 위치를 딕셔너리에 저장하고, 현재 상어 위치를 반환하는 함수
def feed_lst():
    global visited
    global feed_dict

    # 방문 여부를 초기화하고, 먹이 리스트를 초기화
    visited = [[0] * N for _ in range(N)]
    feed_dict = {}

    # 맵을 순회하며 먹이와 상어의 위치를 확인
    for i in range(N):
        for j in range(N):
            # 물고기가 존재할 때
            if 1 <= ocean[i][j] <= 6 :
                # 상어보다 크기가 작은 물고기만 먹이 리스트에 추가
                if ocean[i][j] < shark_size:
                    feed_dict[(i, j)] = ocean[i][j]

                # 상어보다 큰 물고기가 있는 칸은 방문 불가로 설정
                elif ocean[i][j] > shark_size:
                    visited[i][j] = 1

            # 상어가 있는 칸도 방문 불가로 설정
            if ocean[i][j] == 9:
                visited[i][j] = 1

# 초기 상어의 위치를 찾는 함수
def init_shark():
    for i in range(N):
        for j in range(N):
            if ocean[i][j] == 9:
                return i, j  # 상어의 초기 위치 반환

# 입력 처리 및 초기 설정
N = int(input())
ocean = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
total_time = 0  # 총 소요 시간을 저장하는 변수
temp_time = 0  # 특정 먹이까지의 시간을 계산하는 임시 변수

shark_size = 2  # 초기 상어 크기
cnt_to_grow = shark_size  # 상어가 성장하기 위해 필요한 먹이의 수

feed_dict = {}  # 먹이 리스트 초기화
shark_x, shark_y = init_shark()  # 초기 상어 위치 가져오기

# 초기 먹이 리스트 생성
feed_lst()

# 먹을 수 있는 먹이가 없으면 0 출력 후 종료
if len(feed_dict) == 0:
    print(0)
    exit()

# 상어의 이동을 위한 큐 초기화
shark_que = deque()
shark_que.append((shark_x, shark_y))

# 상하좌우 이동을 위한 방향 벡터 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어가 움직일 수 있는 동안 반복
while len(shark_que) > 0:
    q_size = len(shark_que)
    temp_feed = []  # 이번 턴에 먹을 수 있는 먹이 위치를 저장할 리스트

    # 현재 큐에 있는 모든 위치를 순회
    for _ in range(q_size):
        cx, cy = shark_que.popleft()

        # 네 방향으로 이동을 시도
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]

            # 맵의 경계를 벗어나면 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 이미 방문했거나 상어보다 큰 물고기가 있으면 무시
            if visited[nx][ny] != 0 or ocean[nx][ny] > shark_size:
                continue

            # 이동한 위치에 물고기가 있는 경우
            if ocean[nx][ny] != 0:
                # 먹을 수 있는 먹이라면 (먹이 리스트에 존재한다면)
                if feed_dict.get((nx, ny)) is not None:
                    temp_feed.append((nx, ny))  # 먹이 후보에 추가

                else:
                    shark_que.append((nx, ny))  # 큐에 추가하여 계속 탐색
                    visited[nx][ny] = 1

            else:
                shark_que.append((nx, ny))  # 빈 칸일 경우 이동만 수행
                visited[nx][ny] = 1

    temp_time += 1  # 이번 턴을 소요 시간에 반영

    # 먹을 수 있는 먹이가 발견되었다면
    if len(temp_feed) > 0:
        # 먹이 후보들을 정렬하여 가장 가까운 것 선택 (위쪽, 왼쪽 우선)
        temp_feed.sort(key=lambda x: (-x[0], -x[1]))

        # 현재 상어 위치를 빈 칸으로 만들고, 새로운 위치로 이동
        ocean[shark_x][shark_y] = 0
        shark_x, shark_y = temp_feed.pop()
        ocean[shark_x][shark_y] = 9

        cnt_to_grow -= 1  # 먹이를 먹었으니 성장 조건 감소
        total_time += temp_time  # 먹이를 먹은 경우 시간을 반영
        temp_time = 0  # 임시 시간을 초기화

        # 상어가 성장할 수 있다면 성장
        if cnt_to_grow == 0:
            shark_size += 1
            cnt_to_grow = shark_size

        # 새로 먹이 리스트 갱신
        feed_lst()

        # 더 이상 먹을 수 있는 먹이가 없으면 종료
        if len(feed_dict) == 0:
            print(total_time)
            break

        # 다음 탐색을 위해 큐 초기화 및 현재 상어 위치 추가
        shark_que = deque()
        shark_que.append((shark_x, shark_y))

    # 더 이상 상어가 움직일 수 있는 곳이 없다면 총 시간을 출력하고 종료
    if len(shark_que) == 0:
        print(total_time)
        exit()

# 이 경우는 while 문이 끝날 때까지 탈출 조건이 없었던 경우
