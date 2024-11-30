# 1697 숨바꼭질
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    time = 0

    while q:
        q_size = len(q)
        time += 1
        # print(time, q)
        for _ in range(q_size):
            cx = q.popleft()
            for k in range(3):
                nx = cord_dict[k](cx)

                if nx < 0 or nx > 100000:
                    continue

                if visited[nx]:
                    continue
                   
                if nx == K:
                    return time

                visited[nx] = True

                q.append(nx)
    time -= 1


N, K = map(int, input().split())
if N==K:
    print(0)
    exit()

q = deque()
q.append(N)
visited = [False]*100001
visited[N] = True
cord_dict = {0: lambda x : x+1, 1: lambda x : x-1, 2: lambda x : x*2}

print(bfs())