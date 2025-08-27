
import java.io.*;
import java.util.*;

public class Main {


	static int[] dx = {-1, 1, 0, 0, -1, 1, -1, 1};
	static int[] dy = {0, 0, -1, 1, -1, 1, 1, -1};
	
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            if (w == 0 && h == 0) return;
            
            int count = 0;
            int[][] map = new int[h][w];
            boolean[][] visited = new boolean [h][w];
            
            // map 세팅
            for(int i=0; i<h; i++) {
            	st = new StringTokenizer(br.readLine());
            	
                for(int j=0; j<w; j++) {
                	map[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            
            // BFS
            for(int i=0; i<h; i++) {
                for(int j=0; j<w; j++) {
                	if(map[i][j]==1 && !visited[i][j]) {
                		BFS(i, j, map, visited, w, h); 
                		count++;
                	}
                }
            }
            System.out.println(count);
        }
    }
    
    static void BFS(int cx, int cy, int[][] map, boolean[][] visited, int w, int h) {
    	Queue<int[]> q = new ArrayDeque<>();
    	
    	q.offer(new int[] {cx, cy});
    	visited[cx][cy] = true;
    	
    	while(!q.isEmpty()) {
    		int[] cur = q.poll();
    		int x = cur[0], y = cur[1];
    		
    		for (int dir=0; dir<8; dir++) {
    			int nx = x + dx[dir];
    			int ny = y + dy[dir];
    			
    			if (nx<0 || nx>=h || ny<0 || ny>=w) continue;
    			if (visited[nx][ny]) continue;
    			if (map[nx][ny] == 0) continue;
    			
    			visited[nx][ny] = true;
    			q.offer(new int[] {nx, ny});
    		}    		
    	}
    }

}
