case = int(input())

for _ in range(case):
    
    n,m = map(int, input().split())
    que = list(map(int, input().split()))
    que_check = [0 for _ in range(n)]
    que_check[m] = 1
    order = 0
    
    while True:
        if que[0] == max(que):
            if que_check[0] == 1:
                order += 1
                print(order)
                break
            else:
                order += 1
                que.pop(0)
                que_check.pop(0)
        else:
            que.append(que.pop(0))
            que_check.append(que_check.pop(0))