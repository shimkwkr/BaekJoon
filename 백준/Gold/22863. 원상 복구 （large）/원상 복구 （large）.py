# 입력 받기
N, K = map(int, input().split())
S = list(map(int, input().split()))
D = [x-1 for x in map(int, input().split())]  # 0-based indexing으로 변경

# 결과와 방문 체크 배열
visited = [False] * N
result = [0] * N

# 각 위치에 대해
for i in range(N):
    if not visited[i]:
        # 현재 순환 사이클 찾기
        cycle = []
        cur = i
        
        while not visited[cur]:
            visited[cur] = True
            cycle.append(cur)
            cur = D[cur]
        
        # K번 이동 후의 위치 계산하고 결과 저장
        cycle_len = len(cycle)
        for j in range(cycle_len):
            pos = cycle[(j + K) % cycle_len]
            result[pos] = S[cycle[j]]

# 결과 출력
print(*result)