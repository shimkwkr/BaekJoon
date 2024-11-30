# 2143. G3 두 배열의 합
import sys
input = sys.stdin.readline

T = int(input())

n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))


for i in range(n):
    num = A[i]
    for j in range(i+1, n):
        num += A[j]
        A.append(num)

for i in range(m):
    num = B[i]
    for j in range(i+1, m):
        num += B[j]
        B.append(num)

A.sort()
B.sort(reverse=True)

A_s = 0
B_s = 0
cnt = 0

ln_A = len(A)
ln_B = len(B)

while A_s < ln_A and B_s < ln_B:
    target = A[A_s] + B[B_s]

    if target > T:
        B_s += 1
    elif target < T:
        A_s += 1
    else:
        temp_A_s = A_s
        temp_B_s = B_s

        while A[temp_A_s] == A[A_s]:
            temp_A_s += 1
            if temp_A_s == ln_A:
                break

        while B[temp_B_s] == B[B_s]:
            temp_B_s += 1
            if temp_B_s == ln_B:
                break

        cnt += (temp_A_s-A_s) * (temp_B_s-B_s)
        A_s = temp_A_s
        B_s = temp_B_s

print(cnt)

