import java.io.*;
import java.util.*;

public class Main {
	
	static int[] ans;
	static boolean[] visit;
	static boolean[] cycleNodes;
	static List<Integer>[] graph;
	
	public static void main (String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());		
		ans = new int[N+1];
		Arrays.fill(ans, -1);
		
		graph = new ArrayList[N+1];
		cycleNodes = new boolean[N+1];
		
		for(int i=0; i<=N; i++) {
			graph[i] = new ArrayList<>();
		}
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());			
			graph[u].add(v);
			graph[v].add(u);
		}
		
		for(int i=1; i<=N; i++) {
			visit = new boolean[N+1];
			if(isCycle(i, i, -1)){
				cycleNodes[i]=true;
				ans[i] = 0;
			}
		}
		
		bfsFromCycleNodes(N);
		
		for(int i=1; i<ans.length; i++) {
			System.out.print(ans[i] + " ");
		}
	}
	
	// 노드가 Cycle의 포함 여부 - DFS 이용
	private static boolean isCycle(int start, int cur, int prev) {
		visit[cur] = true;
		
		for (int next : graph[cur]) {
			if (next == prev) continue;
			
			if (!visit[next]) {
				if(isCycle(start, next, cur)) {
					return true;
				}
			} else {
				// 시작한 노드인데 직전 노드가 아닌 경우
				if(next == start) {
					return true;
				}
			}
		}
		return false;
	}
	
	// Cycle로부터의 거리 구하기 - BFS이용
	private static void bfsFromCycleNodes (int N) {
		Queue<Integer> q = new ArrayDeque<>();
		for(int i=0; i<=N; i++) {
			if(cycleNodes[i]) {
				ans[i] = 0;
				q.offer(i);
			}
		}
		
		while(!q.isEmpty()) {
			int cur = q.poll();
			
			for(int next : graph[cur]) {
				if (ans[next] == -1) {
					ans[next] = ans[cur] + 1;
					q.offer(next);
				}
			}
		}
	}	
}
