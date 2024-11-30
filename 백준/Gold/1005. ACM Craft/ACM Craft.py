# 1005 G3 ACM Craft
import sys
from collections import deque
input = sys.stdin.readline

T= int(input())
for tc in range(1, T+1):
    # N은 건물 개수, K는 건설 순서개수(간선)
    N, K = map(int, input().split())
    # 건물 건설 시간
    con_time = deque(map(int, input().split()))
    con_time.appendleft(0)
    # 인접 리스트
    adj = [[] for _ in range(N+1)]
    # 진입 차수
    indegree = [0]*(N+1)
    # dp 배열설정
    dp = [0]*(N+1)

    q = deque()

    for _ in range(K):
        u, v = map(int, input().split())
        adj[u].append(v)
        indegree[v] += 1
    # 백준이가 승리하기 위해 건설해야 할 건물 번호
    W = int(input())

    for i in range(len(indegree)):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = con_time[i]

    if indegree[W] == 0:
        print(con_time[W])
        continue

    while q:
        now = q.popleft()

        for i in adj[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
            dp[i] = max(dp[i], dp[now]+ con_time[i])

        if indegree[W] == 0:
            break
    print(dp[W])