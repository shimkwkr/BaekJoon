# 12738 가장 긴 증가하는 부분 수열 3

def bin_srch(target):
    start = 0
    end = len(LIS)-1
    
    while start <= end:
        mid = (start + end) // 2
        if LIS[mid] > target:
            end = mid-1
        elif LIS[mid] < target:
            start = mid+1
        else:
            return mid
    
    return start        

N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]

for i in range(N):
    if LIS[-1] < A[i]:
        LIS.append(A[i])
    
    else:
        idx = bin_srch(A[i])
        LIS[idx] = A[i]
        
print(len(LIS))        