import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int,input().split()))
dp = [0]

for i in box:
    if i > dp[-1]:
        dp.append(i)
        continue
    for j in range(len(dp)-1,-1,-1):
        if i > dp[j]:
            dp[j+1] = i
            break
print(len(dp)-1)