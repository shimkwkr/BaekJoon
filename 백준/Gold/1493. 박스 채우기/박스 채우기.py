# 1493 G2 박스 채우기
import sys
input = sys.stdin.readline

length, width, height = map(int, input().split())

N = int(input())

total_cube = 0
total_volume = 0
acc = 0
cube_inf = []

for i in range(N):
    len_cube, cnt_cube = map(int ,input().split())

    len_cube = 2**len_cube
    cube_inf.append([len_cube, cnt_cube])

cube_inf.sort(reverse=True)

for i in range(N):
    acc *= 8
    len_cube, cnt_cube = cube_inf[i][0], cube_inf[i][1]
    used_cube = (length//len_cube) * (width//len_cube) * (height//len_cube) - acc
    used_cube = min(used_cube, cnt_cube)

    if used_cube > 0:
        acc += used_cube
        total_cube += used_cube
        total_volume += used_cube * len_cube**3

if total_volume == length*width*height:
    print(total_cube)
else:
    print(-1)
