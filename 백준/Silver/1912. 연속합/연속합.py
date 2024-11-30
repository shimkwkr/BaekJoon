# 1912. 연속합

n = int(input())
m = list(map(int, input().split()))

dp = [0]*n
dp[0] = m[0]

for i in range(1,n):
    dp[i] = max(dp[i-1] + m[i], m[i])

print(max(dp))