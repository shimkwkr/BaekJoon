# 1305 P4. 광고

def kmp(pattern):

    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        while i>0 and pattern[i] != pattern[j]:
            i = table[i-1]
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i

    return L - table[-1]

L = int(input())
ad = input()

print(kmp(ad))
