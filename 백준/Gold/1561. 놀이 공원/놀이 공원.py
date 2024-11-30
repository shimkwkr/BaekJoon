# 1561. 놀이공원
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rides = list(map(int, input().split()))

start = 0
end = 60000000000
last_time = 0
cnt = M

if N<M:
    print(N)
else:
    while start<=end:
        mid = (start + end)//2
        rided_people = M

        for i in range(M):
            rided_people += (mid // rides[i])

        if rided_people >= N:
            last_time = mid
            end = mid - 1
        else:
            start = mid + 1

    # last_time - 1 까지 놀이기구를 탄 사람들의 수를 cnt에 계산
    for i in range(M):
        cnt += ((last_time-1) // rides[i])

    # last_time 에 놀이기구를 탄 사람을 search
    for i in range(M):
        if last_time % rides[i] == 0:
            cnt+=1
        if cnt == N:
            print(i+1)
            break