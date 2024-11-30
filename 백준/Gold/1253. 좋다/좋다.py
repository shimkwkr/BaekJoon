# 1253 G4 좋다

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
good = 0
end_init = len(arr)-1

for i in range(N):
    goal = arr[i]
    start = 0
    end = end_init
    
    while start < end:
        if arr[start] + arr[end] == goal:
            # 어떤 수가 다른 수 두 개의 합으로 나타낼수 있어야 하므로
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                good += 1
                break
        
        elif arr[start] + arr[end] > goal:
            end -= 1
        else:
            start += 1

print(good)            