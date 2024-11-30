# 꼬인 전깃줄

import sys
input = sys.stdin.readline

def bin_srch(target):
    start = 0
    end = len(lis_temp)-1

    while start<=end:
        mid = (start+end)//2
        if target < lis_temp[mid]:
            end = mid-1
        elif target > lis_temp[mid]:
            start = mid + 1
        else:
            return mid

    return start



# 배열의 크기
n = int(input())

line = list(map(int, input().split()))
# LIS = []

lis_temp = [-float('inf')]
lis_inf = [(-float('inf'), 0)]

for i in range(n):
    if lis_temp[-1] < line[i]:
        lis_temp.append(line[i])
        lis_inf.append( (line[i], len(lis_temp)-1) )
        # print(lis_temp, end='111111')
        # print()
    else:
        idx = bin_srch(line[i])
        lis_temp[idx] = line[i]
        lis_inf.append( (line[i], idx) )
        # print(lis_temp, end='2222222')
        # print()

print(n - (len(lis_temp)-1))
# print(lis_inf)


