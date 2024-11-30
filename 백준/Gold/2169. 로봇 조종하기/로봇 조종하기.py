import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dp = []
for i in range(N):
    dp.append(list(map(int, input().split())))
for i in range(1, M):
    dp[0][i] += dp[0][i - 1]
for i in range(1, N):
    dplr = dp[i][:]
    dprl = dp[i][:]
    for j in range(M):
        if j == 0:
            dplr[j] += dp[i - 1][j]
            dprl[M - 1 - j] += dp[i - 1][M - 1 - j]
        else:
            dplr[j] += max(dp[i - 1][j], dplr[j - 1])
            dprl[M - 1 - j] += max(dp[i - 1][M - 1 - j], dprl[M - j])
    for j in range(M):
        dp[i][j] = max(dplr[j], dprl[j])
print(dp[-1][-1])