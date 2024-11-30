# 2632 피자판매
import sys

input = sys.stdin.readline

ordered_size = int(input())
m, n = map(int, input().split())
A = []
B = []

for _ in range(m):
    A.append(int(input()))

for _ in range(n):
    B.append(int(input()))

# 각 피자 조각의 연속된 수의 합들을 구한다(원형 큐)
A_pizza = [0]
B_pizza = [0]

# 한번 순회하면서 연속된 부분합 구하는 로직
totall = 0
for i in range(len(A)):
    totall += A[i]
    cnt = 0
    for j in range(i, i + len(A) - 1):
        cnt += A[j % len(A)]
        A_pizza.append(cnt)

A_pizza.append(totall)


totall = 0
for i in range(len(B)):
    totall += B[i]
    cnt = 0
    for j in range(i, i + len(B) - 1):
        cnt += B[j % len(B)]
        B_pizza.append(cnt)

B_pizza.append(totall)

A_pizza.sort()
B_pizza.sort(reverse=True)

# print(A_pizza)
# print(B_pizza)

A_s = 0
B_s = 0

cnt = 0
while A_s < len(A_pizza) and B_s < len(B_pizza):
    mid = A_pizza[A_s] + B_pizza[B_s]

    if mid > ordered_size:
        B_s += 1

    elif mid < ordered_size:
        A_s += 1

    else:
        temp_A = A_s
        temp_B = B_s
        while A_pizza[temp_A] == A_pizza[A_s]:
            temp_A += 1
            if temp_A == len(A_pizza):
                break
        while B_pizza[temp_B] == B_pizza[B_s]:
            temp_B += 1
            if temp_B == len(B_pizza):
                break

        cnt += (temp_A - A_s) * (temp_B - B_s)
        # print(temp_A, temp_B, A_s, B_s, cnt)
        A_s = temp_A
        B_s = temp_B

print(cnt)
