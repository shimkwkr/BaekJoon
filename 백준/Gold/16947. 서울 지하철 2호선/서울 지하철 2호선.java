import java.io.*;
import java.util.*;

public class Main {
	
	static int[] distance;
	static boolean[] visited;
	static boolean[] isCycleNode;
	static List<Integer>[] adjList;
	
	public static void main (String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		distance = new int[N+1];
		Arrays.fill(distance, -1);
		
		isCycleNode = new boolean[N+1];
		adjList = new ArrayList[N+1];
		
		for (int i=0; i<=N; i++) {
			adjList[i] = new ArrayList<>();
		}
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			adjList[u].add(v);
			adjList[v].add(u);
		}
		
		// 어떤 노드가 Cycle에 포함되어 있는지 확인후 isCycleNode에 기록
		for(int i=1; i<=N; i++) {
			visited = new boolean[N+1];
			
			if(isCycle(i, i, -1)) {
				isCycleNode[i] = true;
				distance[i] = 0;
			}
		}
		
		calculateDistanceFromCycle(N);
		
		for(int i=1; i<=N; i++) {
			System.out.print(distance[i] + " ");
		}
	}
	
	// Cycle에 포함되어 있는지 아닌지 - DFS
	private static boolean isCycle(int start, int cur, int prev) {
		visited[cur] = true;
		
		for(int next : adjList[cur]) {
			if (next == prev) {
				continue;
			}
			
			// 아직 방문하지 않은 정점이라면?
			if (!visited[next]) {
				// 계속 DFS탐색을 진행
				if(isCycle(start, next, cur)) {
					return true;					
				}
			} else {
				// 시작한 노드인데 직전 노드가 아닌 경우
				if (next == start) {
					return true;
				}
			}
		}
		return false;
	}
	
	private static void calculateDistanceFromCycle(int N) {
		Queue<Integer> q = new ArrayDeque<>();
		
		for(int i=1; i<=N; i++) {
			if(distance[i] == 0) {
				q.offer(i);
			}
		}
		
		while(!q.isEmpty()) {
			int cur = q.poll();
			
			for(int next : adjList[cur]) {
				if(distance[next] == -1) {
					distance[next] = distance[cur] +1;
					q.offer(next);
				}
			}
		}
	}
}
