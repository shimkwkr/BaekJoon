# 21276. G2 계보 복원가 호석
import sys
from collections import deque
input = sys.stdin.readline

# 석호촌 거주자 수
N = int(input())
# 살고 있는 사람들의 이름
person_lst = list(input().split())

# u-> v 자식 -> 부모, v->u 부모 -> 자식
adj_u_v = [[] for _ in range(N+1)]
adj_v_u = [[] for _ in range(N+1)]
dict_p_idx = {}
dict_idx_p = {}

# 조상 -> 자식 의 인접정보
indegree = [0]*(N+1)

temp = 1
for i in range(len(person_lst)):
    dict_p_idx[person_lst[i]] = temp
    dict_idx_p[temp] = person_lst[i]
    temp += 1

# 기억하는 정보의 개수
M = int(input())

# 기억하는 정보
for _ in range(M):
    u, v = input().split()
    adj_u_v[dict_p_idx[u]].append(dict_p_idx[v])
    adj_v_u[dict_p_idx[v]].append(dict_p_idx[u])
    indegree[dict_p_idx[u]] += 1

# print(dict_p_idx)
# print(dict_idx_p)
# print(adj_u_v)
# print(adj_v_u)
# print(indegree)

# 첫번째 출력 : 가문의 개수 K
K = 0
q = deque()
root = []
for i in range(1, len(adj_u_v)):
    if len(adj_u_v[i]) == 0:
        K += 1
        # 두번째 출력을 위한 각 가문 시조의 이름 넣기
        root.append(dict_idx_p[i])
        q.append(i)
print(K)

# 두 번째 출력: 각 시조들의 이름을 공백으로 구분하여 사전순으로 출력
root.sort()
print(*root)

# 세번째 출력 : 사전순 대로 사람의 이름, 그 사람의 자식의수,
# 그리고 사전순으로 자식들의 이름을 공백으로 구분해 출력
person_lst.sort()
childs = [[] for _ in range(N+1)]

while q:
    now = q.popleft()
    for i in adj_v_u[now]:
         indegree[i]-=1
         if indegree[i] == 0:
             childs[now].append(dict_idx_p[i])
             q.append(i)

for i in range(N):
    print(person_lst[i], len(childs[dict_p_idx[person_lst[i]]]), *sorted(childs[dict_p_idx[person_lst[i]]]))