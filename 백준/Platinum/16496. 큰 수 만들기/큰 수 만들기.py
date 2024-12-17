# 16496 P5. 큰 수 만들기

N = int(input())

arr = list(input().split())
# print(arr)

'''
4
341 34 30 3
'''

temp = []
for num in arr:
    a = num
    while len(num) < 10:
        num += num

    num = num[:10]
    temp.append((int(num), a))
temp.sort(reverse=True)
# print(temp)

result = []
for i in temp:
    result.append(i[1])

answer = ''.join(result)

if answer[0] == '0':
    print(0)
else:
    print(answer)

