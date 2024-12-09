# 10266 P4 시계 사진들

def kmp(all_string, pattern):

    table = [0 for _ in range(len(pattern))]
    i = 0

    for j in range(1, len(pattern)):
        while i>0 and pattern[i] != pattern[j]:
            i = table[i-1]
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i

    i = 0
    for j in range(len(all_string)):
        while i > 0 and all_string[j] != pattern[i]:
            i = table[i-1]
        if all_string[j] == pattern[i]:
            i += 1
            if i == len(pattern):
                return True

    return False

n = int(input())

all_string = [0]*720000
pattern = [0]*360000

clock1 = list(map(int, input().split()))
clock2 = list(map(int, input().split()))

for i in range(n):
    all_string[clock1[i]], all_string[clock1[i]+360000] = 1, 1
    pattern[clock2[i]] = 1

if kmp(all_string, pattern):
    print('possible')
else:
    print('impossible')

