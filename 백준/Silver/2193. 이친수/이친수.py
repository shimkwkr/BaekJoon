N=int(input())
dp=[1,1]
if N==1:
    print(1)
elif N==2:
    print(1)
else:
    for i in range(2,N):
        dp.append(dp[i-1]+dp[i-2])
    print(dp[N-1])