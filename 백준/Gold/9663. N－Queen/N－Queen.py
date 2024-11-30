def back(q):
  global n, cnt
  if q == n:
    cnt += 1
    return
    
  for i in range(n):
    if not queen[i] and not queen_up[q+i] and not queen_down[(n-1)+q-i]:
      queen[i] = True
      queen_up[q+i] = True
      queen_down[(n-1)+q-i] = True
      back(q+1)
      queen[i] = False
      queen_up[q+i] = False
      queen_down[(n-1)+q-i] = False
            
n = int(input())
cnt = 0

# 세로
queen = [False]*n
# 위로 사선 y = x
queen_up = [False]*(2*n-1)
# 아래 사선 y = -x
queen_down = [False]*(2*n-1)
back(0)

print(cnt)