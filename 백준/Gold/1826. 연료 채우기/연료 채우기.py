# 1826. G2 연료 채우기

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
stations = []
cnt = 0

for i in range(N):
    pos, can_charge = map(int, input().split())
    heappush(stations, (pos, can_charge))

village, cur_gas = map(int, input().split())

passed_stations = []
while stations:
    pos, can_charge = heappop(stations)

    if pos <= cur_gas:
        heappush(passed_stations, (-can_charge, pos))

    else:
        while passed_stations and cur_gas < pos:
            c, p = heappop(passed_stations)
            cur_gas -= c
            cnt += 1

        if cur_gas < pos:
            print(-1)
            exit()

        heappush(passed_stations, (-can_charge, pos))

while passed_stations and cur_gas < village:
    can_charge, pos = heappop(passed_stations)
    cur_gas -= can_charge
    cnt += 1

if cur_gas < village:
    print(-1)
else:
    print(cnt)
