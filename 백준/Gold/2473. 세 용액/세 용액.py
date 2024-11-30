# 2473 G3 세 용액

N = int(input())

arr = list(map(int, input().split()))
arr.sort()

mix = float('inf')

for start in range(N-2):
    mid = start + 1
    end = N-1
    while mid < end:
        temp = arr[start] + arr[mid] + arr[end]
        if mix > abs(temp):
            mix = abs(temp)
            result_1, result_2, result_3 = arr[start], arr[mid], arr[end]
        
        if temp > 0:
            end -= 1
        elif temp < 0:
            mid += 1
        else:
            print(arr[start], arr[mid], arr[end])        
            exit()
    
    
print(result_1, result_2, result_3)