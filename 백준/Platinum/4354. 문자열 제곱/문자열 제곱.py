# 4354. P4 문자열 제곱

def kmp(all_string):
    table = [0 for _ in range(len(all_string))]
    i = 0

    for j in range(1, len(all_string)):
        while i>0 and all_string[i] != all_string[j]:
            i = table[i-1]

        if all_string[i] == all_string[j]:
            i += 1
            table[j] = i

    if len(all_string) % (len(all_string) - table[-1]) != 0:
        return 1
    else: 
        return len(all_string) // (len(all_string) - table[-1])

while True:
    all_string = input()
    if all_string == '.':
        break

    print(kmp(all_string))