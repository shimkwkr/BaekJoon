# 12100. 2048(easy)

# 백트레킹 - 상하좌우 각각 이동시킨경우에도 이동 전과 결과가 같은경우 가지치기
def back(arr, n, max_num):

    # 최대 5번 이동시킬것이므로
    if n == 5:
        return max_num

    left_result, left_max = left(arr)
    right_result, right_max = right(arr)
    up_result, up_max = up(arr)
    down_result, down_max = down(arr)

    # print('left')
    # for i in left_result:
    #     print(*i)
    # print('right')
    # for i in right_result:
    #     print(*i)
    # print('up')
    # for i in up_result:
    #     print(*i)
    # print('down')
    # for i in down_result:
    #     print(*i)

    a,b,c,d = left_max,right_max,up_max,down_max

    # 만약 이동 전과 이동 후의 결과가 같다면 pruning
    if arr != left_result:
        # 왼쪽으로 옮 녀석으로 다시 실행
        a = back(left_result, n + 1, left_max)
        # print(a, 1)

    if arr != right_result:
        # 오른쪽으로 옮긴...
        b = back(right_result, n + 1, right_max)
        # print(b,2)

    if arr != up_result:
        # 위쪽으로 옮긴...
        c = back(up_result, n + 1, up_max)
        # print(c,3)

    if arr != down_result:
        # 아래쪽으로 옮긴...
        d = back(down_result, n + 1, down_max)
        # print(d,4)

    return max(a,b,c,d)

# 왼쪽으로 옮겼을때
def left(arr):
    # 왼쪽으로 옮길 녀석을 복사하여 생성 (deep copy)
    temp_arr_left = [arr[i][:] for i in range(N)]
    max_block_num = temp_arr_left[0][0]
    for i in range(N):
        temp = []
        jump_j = 0
        while 0 in temp_arr_left[i]:
            temp_arr_left[i].remove(0)

        for j in range(len(temp_arr_left[i])):

            # jump_j 가 1 이면 이번블럭의 숫자는 확인하지않고 넘김
            if jump_j == 1:
                jump_j = 0
                continue

            # j가 마지막 숫자라면 아래 j+1에서 error가 뜨므로 예외처리
            if j == len(temp_arr_left[i]) - 1:
                temp.append(temp_arr_left[i][j])
                continue

            # 바로 다음 블럭과 숫자를 비교, 다르면 그냥 temp에 append
            if temp_arr_left[i][j] != temp_arr_left[i][j + 1]:
                temp.append(temp_arr_left[i][j])

                # max_block_num값을 비교
                if max_block_num < temp_arr_left[i][j]:
                    max_block_num = temp_arr_left[i][j]

                # 바로 다음 블럭과 숫자를 비교, 다르면 현재숫자를 2배후 temp에 append
            # 이후 다음 블럭은 확인해주지않음
            else:
                temp.append(temp_arr_left[i][j] * 2)
                jump_j = 1

                # max_block_num값을 비교
                if max_block_num < temp_arr_left[i][j]*2:
                    max_block_num = temp_arr_left[i][j]*2

        while len(temp) < N:
            temp.append(0)

        temp_arr_left[i] = temp[:]
    return temp_arr_left, max_block_num


# 오른쪽으로 옮겼을때
def right(arr):
    # 오른쪽으로 옮길 녀석을 복사하여 생성 (deep copy)
    temp_arr_right = [arr[i][:] for i in range(N)]
    max_block_num = temp_arr_right[0][0]
    for i in range(N):
        temp = []
        jump_j = 0
        while 0 in temp_arr_right[i]:
            temp_arr_right[i].remove(0)

        temp_arr_right[i].reverse()
        for j in range(len(temp_arr_right[i])):

            # jump_j 가 1 이면 이번블럭의 숫자는 확인하지않고 넘김
            if jump_j == 1:
                jump_j = 0
                continue

            # j가 마지막 숫자라면 아래 j+1에서 error가 뜨므로 예외처리
            if j == len(temp_arr_right[i]) - 1:
                temp.append(temp_arr_right[i][j])
                continue

            # 바로 다음 블럭과 숫자를 비교, 다르면 그냥 temp에 append
            if temp_arr_right[i][j] != temp_arr_right[i][j + 1]:
                temp.append(temp_arr_right[i][j])

                # max_block_num값을 비교
                if max_block_num < temp_arr_right[i][j]:
                    max_block_num = temp_arr_right[i][j]

                # 바로 다음 블럭과 숫자를 비교, 다르면 현재숫자를 2배후 temp에 append
            # 이후 다음 블럭은 확인해주지않음
            else:
                temp.append(temp_arr_right[i][j] * 2)
                jump_j = 1

                # max_block_num값을 비교
                if max_block_num < temp_arr_right[i][j] * 2:
                    max_block_num = temp_arr_right[i][j] * 2

        while len(temp) < N:
            temp.append(0)

        # 왼쪽과는 다르게 temp를 좌우 반전해줘야한다!!!!
        temp_arr_right[i] = temp[::-1]

    return temp_arr_right, max_block_num


# 위쪽으로 옮겼을때
def up(arr):
    # 위쪽으로 옮길 녀석을 복사하여 생성 (deep copy)
    temp_arr_up = [arr[i][:] for i in range(N)]

    # symetric 시켜줌
    for i in range(N):
        for j in range(N):
            if i < j:
                temp_arr_up[i][j], temp_arr_up[j][i] = temp_arr_up[j][i], temp_arr_up[i][j]

    max_block_num = temp_arr_up[0][0]
    for i in range(N):
        temp = []
        jump_j = 0
        while 0 in temp_arr_up[i]:
            temp_arr_up[i].remove(0)

        for j in range(len(temp_arr_up[i])):

            # jump_j 가 1 이면 이번블럭의 숫자는 확인하지않고 넘김
            if jump_j == 1:
                jump_j = 0
                continue

            # j가 마지막 숫자라면 아래 j+1에서 error가 뜨므로 예외처리
            if j == len(temp_arr_up[i]) - 1:
                temp.append(temp_arr_up[i][j])
                continue

            # 바로 다음 블럭과 숫자를 비교, 다르면 그냥 temp에 append
            if temp_arr_up[i][j] != temp_arr_up[i][j + 1]:
                temp.append(temp_arr_up[i][j])

                # max_block_num값을 비교
                if max_block_num < temp_arr_up[i][j]:
                    max_block_num = temp_arr_up[i][j]

                # 바로 다음 블럭과 숫자를 비교, 다르면 현재숫자를 2배후 temp에 append
            # 이후 다음 블럭은 확인해주지않음
            else:
                temp.append(temp_arr_up[i][j] * 2)
                jump_j = 1

                # max_block_num값을 비교
                if max_block_num < temp_arr_up[i][j] * 2:
                    max_block_num = temp_arr_up[i][j] * 2

        while len(temp) < N:
            temp.append(0)

        temp_arr_up[i] = temp[:]

    # symetric 시켜줌
    for i in range(N):
        for j in range(N):
            if i < j:
                temp_arr_up[i][j], temp_arr_up[j][i] = temp_arr_up[j][i], temp_arr_up[i][j]

    return temp_arr_up, max_block_num

# 아래쪽으로 옮겼을때
def down(arr):
    # 아래쪽으로 옮길 녀석을 복사하여 생성 (deep copy)
    temp_arr_down = [arr[i][:] for i in range(N)]

    # symetric 시켜줌
    for i in range(N):
        for j in range(N):
            if i < j:
                temp_arr_down[i][j], temp_arr_down[j][i] = temp_arr_down[j][i], temp_arr_down[i][j]

    max_block_num = temp_arr_down[0][0]
    for i in range(N):
        temp = []
        jump_j = 0
        while 0 in temp_arr_down[i]:
            temp_arr_down[i].remove(0)

        temp_arr_down[i].reverse()

        for j in range(len(temp_arr_down[i])):

            # jump_j 가 1 이면 이번블럭의 숫자는 확인하지않고 넘김
            if jump_j == 1:
                jump_j = 0
                continue

            # j가 마지막 숫자라면 아래 j+1에서 error가 뜨므로 예외처리
            if j == len(temp_arr_down[i]) - 1:
                temp.append(temp_arr_down[i][j])
                continue

            # 바로 다음 블럭과 숫자를 비교, 다르면 그냥 temp에 append
            if temp_arr_down[i][j] != temp_arr_down[i][j + 1]:
                temp.append(temp_arr_down[i][j])

                # max_block_num값을 비교
                if max_block_num < temp_arr_down[i][j]:
                    max_block_num = temp_arr_down[i][j]

                # 바로 다음 블럭과 숫자를 비교, 다르면 현재숫자를 2배후 temp에 append
            # 이후 다음 블럭은 확인해주지않음
            else:
                temp.append(temp_arr_down[i][j] * 2)
                jump_j = 1

                # max_block_num값을 비교
                if max_block_num < temp_arr_down[i][j] * 2:
                    max_block_num = temp_arr_down[i][j] * 2

        while len(temp) < N:
            temp.append(0)

        temp_arr_down[i] = temp[::-1]

    # symetric 시켜줌
    for i in range(N):
        for j in range(N):
            if i < j:
                temp_arr_down[i][j], temp_arr_down[j][i] = temp_arr_down[j][i], temp_arr_down[i][j]

    return temp_arr_down, max_block_num


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(back(board, 0, 2))
