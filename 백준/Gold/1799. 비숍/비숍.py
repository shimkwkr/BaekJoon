def solve():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 흑백 구분을 위한 비숍 위치 리스트
    white_positions = []
    black_positions = []

    # 비숍을 놓을 수 있는 위치를 색깔별로 분류
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if (i + j) % 2 == 0:
                    white_positions.append((i, j))
                else:
                    black_positions.append((i, j))

    # 각 대각선 방향 방문 체크를 위한 배열
    def bishop_count(positions):
        if not positions:
            return 0

        n = len(positions)
        diag1 = [0] * (2 * N)  # / 방향 대각선
        diag2 = [0] * (2 * N)  # \ 방향 대각선

        def backtrack(idx, count):
            if idx == n:
                return count

            max_count = count
            x, y = positions[idx]

            # 현재 위치에 비숍을 놓을 수 있는 경우
            if not diag1[x + y] and not diag2[x - y + N - 1]:
                diag1[x + y] = 1
                diag2[x - y + N - 1] = 1
                max_count = max(max_count, backtrack(idx + 1, count + 1))
                diag1[x + y] = 0
                diag2[x - y + N - 1] = 0

            # 현재 위치에 비숍을 놓지 않는 경우
            max_count = max(max_count, backtrack(idx + 1, count))

            return max_count

        return backtrack(0, 0)

    # 흑색과 백색 위치에서 각각 최대 비숍 수를 구하고 합산
    return bishop_count(white_positions) + bishop_count(black_positions)


print(solve())