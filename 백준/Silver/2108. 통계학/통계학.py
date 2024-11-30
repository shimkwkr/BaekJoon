import sys

N = int(input())
num_list = []
sum = 0

for i in range(N):
    num_list.append(int(sys.stdin.readline()))

sort_num_list = sorted(num_list)

# 1. 산술 평균
for i in range(len(num_list)):
    sum += num_list[i] # 산술평균 sum

avg = round(sum/len(num_list))

# 2. 중앙값
mid_num = sort_num_list[len(sort_num_list)//2]

# 3. 최빈값
def mode (num_list): # 최빈값
    count_dict = {}

    # num_list 를 돌면서 count_dict에 없으면 1로 있으면 해당 value를 +1 하는식으로 count
    for num in sort_num_list:
        if num in count_dict:
            count_dict[num] += 1
        else :
            count_dict[num] = 1
    #print(count_dict)
    max_count = max(count_dict.values())
    mode_list = []
    # print(f'count_list : {count_list}')


    for key, value in count_dict.items():
        if value == max_count:
            mode_list.append(key)

    #print(mode_list)
    mode_list_sort = sorted(mode_list)

    if len(mode_list) > 1:
        return mode_list_sort[1]
    else:
        return mode_list_sort[0]

# # num_count[0~4000] 은 숫자 0~4000이 나온 빈도수
# # num_count[4001~8000] 은 숫자 -1부터 -4000이 나온 빈도수
# num_count = [0]*8001
# for num in num_list:
#
#     # num값이 양수면 num_count의 num번방의 숫자를 +1
#     if num >= 0:
#         num_count[num] += 1
#     # num값이 음수면 num_count의 -num+4000번방의 숫자를 +1
#     else :
#         num_count[-num + 4000] += 1
#
# #num_count[ 0 0 1 2 3 2 3 1 ].
# #num_list [ 0 1 2 3 4 5 6 7 ]
#
# max_num = 0
#
# for i in range(len(num_count)):
#     if num_count[i] > max_num:
#         max_num = num_count[i]
#         index = i
#
# max_list = []
# for i in range(len(num_count)):
#     if max_num == num_count[i] and i != index:
#         max_list.append(i)
#
# print(max_list[1])
#
#
# for i in range(len(num_count)):


# 4. 범위
max_min_diff = sort_num_list[len(sort_num_list)-1] - sort_num_list[0]

print(avg)
print(mid_num)
print(mode(num_list))
print(max_min_diff)