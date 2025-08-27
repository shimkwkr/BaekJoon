import java.io.*;
import java.util.*;

public class Main {
	
	static int N, M;
	static int days = -1;
	static int[][] box;
	static final int[] dx = {1, -1, 0, 0};
	static final int[] dy = {0, 0, 1, -1};
	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		
		box = new int[N][M];
		Queue<int[]> q = new ArrayDeque<>();
		
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<M; j++) {
				box[i][j] = Integer.parseInt(st.nextToken());
				if (box[i][j] == 1) {
					q.offer(new int[] {i, j});
				} 
			}
		}
		
		while (!q.isEmpty()) {
			int len = q.size();
			days += 1;
			
			for (int i=0; i<len; i++) {
				int[] cur = q.poll();
				int cx = cur[0], cy = cur[1];
				
				for (int dir=0; dir<4; dir++) {
					int nx = cx + dx[dir];
					int ny = cy + dy[dir];
					
					if (nx<0 || nx>=N || ny<0 || ny>=M) continue;
					if (box[nx][ny] != 0) continue;
					
					box[nx][ny] = 1;
					q.offer(new int[] {nx, ny});
				}
				
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (box[i][j] == 0) {
					System.out.println(-1);
					return;
				}
			}
		}
		if (days == -1) days = 0;
		System.out.println(days);
	}
}
