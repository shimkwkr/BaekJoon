# 15663 N과M (9)

def back():
    check = 0
    if len(result) == M:
        print(*result)
        return

    for i in range(N):
        if visited[i] == 0 and lst[i] != check:

            result.append(lst[i])
            visited[i] = 1
            check = lst[i]

            back()

            result.pop()
            visited[i] = 0


N, M = map(int,input().split())
lst = sorted(list(map(int,input().split())))
result = []
visited = [0]*N
back()
