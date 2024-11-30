import sys
input = sys.stdin.readline

n, m = map(int,input().split())
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    day, page = map(int,input().split())

    for j in range(1, n + 1):        
        if j - day >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - day] + page)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])