def bak(rm_node_num):
    p_node[rm_node_num] = -2

    for i in range(len(p_node)):
        if rm_node_num == p_node[i]:
            bak(i)


N = int(input())
p_node = list(map(int, input().split()))
rm_node_num = int(input())
cnt = 0

bak(rm_node_num)

for i in range(len(p_node)):
    if p_node[i] != -2 and i not in p_node:
        cnt += 1

print(cnt)