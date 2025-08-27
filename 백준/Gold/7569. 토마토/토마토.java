
import java.io.*;
import java.util.*;

public class Main {
	
	static int days = -1;
	static int[][] box;
	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		int H = Integer.parseInt(st.nextToken());
		
		box = new int[N*H][M];
		Queue<int[]> q = new ArrayDeque<>();
		
		for(int i=0; i<N*H; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<M; j++) {
				box[i][j] = Integer.parseInt(st.nextToken());
				if(box[i][j]==1) {
					q.offer(new int[] {i, j});
				}
			}
		}
		
		final int[] dx = {1, -1, 0, 0, N, -N};
		final int[] dy = {0, 0, 1, -1, 0, 0};
		
		while(!q.isEmpty()) {
			int len = q.size();
			days += 1;
			
			for (int i=0; i<len; i++) {
				int [] cur = q.poll();
				int cx = cur[0], cy= cur[1];
				
				
				for (int dir=0; dir<6; dir++) {
					int nx = cx + dx[dir];
					int ny = cy + dy[dir];
					
					if(dir<4) {
						if(nx<(cx/N)*N || nx>=(cx/N)*N + N || ny<0 || ny>=M) continue;						
					} else {
						if(nx<0 || nx>=N*H || ny<0 || ny>=M) continue;	
					}					
					if(box[nx][ny]!=0) continue;
					
					box[nx][ny] = 1;
					q.offer(new int[] {nx, ny});
					
				}
			}
			
		}
		
		for(int i=0; i<N*H; i++) {
			for(int j=0; j<M; j++) {
				if (box[i][j]== 0) {
					System.out.println(-1);
					return;
				}
			}
		}
		
		if(days == -1) days=0;
		System.out.println(days);
	}
}
