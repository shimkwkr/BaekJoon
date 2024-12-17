from heapq import heappush, heappop
import sys
from collections import deque
input = sys.stdin.readline

def dijkstra(start, end):
    dist = [float('inf')] * N
    dist[start] = 0
    # 경로 추적을 위한 배열
    paths = [[] for _ in range(N)]
    
    pq = [(0, start)]
    
    while pq:
        weight, node = heappop(pq)
        
        if weight > dist[node]:
            continue
            
        for nxt_weight, nxt_node in adj[node]:
            new_weight = weight + nxt_weight
            
            if dist[nxt_node] > new_weight:
                dist[nxt_node] = new_weight
                paths[nxt_node] = [node]
                heappush(pq, (new_weight, nxt_node))
            elif dist[nxt_node] == new_weight:
                paths[nxt_node].append(node)
                
    return dist[end], paths

def remove_shortest_paths(end, paths, dist):
    # 최단 경로에 포함된 간선들을 제거
    dropped = [[False] * N for _ in range(N)]
    q = deque([end])
    
    while q:
        node = q.popleft()
        for prev in paths[node]:
            if not dropped[prev][node]:
                dropped[prev][node] = True
                q.append(prev)
                
    return dropped

def find_almost_shortest(start, end, dropped):
    dist = [float('inf')] * N
    dist[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        weight, node = heappop(pq)
        
        if weight > dist[node]:
            continue
            
        for nxt_weight, nxt_node in adj[node]:
            if dropped[node][nxt_node]:
                continue
                
            new_weight = weight + nxt_weight
            
            if dist[nxt_node] > new_weight:
                dist[nxt_node] = new_weight
                heappush(pq, (new_weight, nxt_node))
    
    return dist[end]

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
        
    S, D = map(int, input().split())
    adj = [[] for _ in range(N)]
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        adj[u].append((w, v))
    
    # 최단 경로 찾기
    shortest_dist, paths = dijkstra(S, D)
    
    if shortest_dist == float('inf'):
        print(-1)
        continue
    
    # 최단 경로에 포함된 간선들 제거
    dropped = remove_shortest_paths(D, paths, shortest_dist)
    
    # 거의 최단 경로 찾기
    almost_shortest = find_almost_shortest(S, D, dropped)
    
    print(almost_shortest if almost_shortest != float('inf') else -1)