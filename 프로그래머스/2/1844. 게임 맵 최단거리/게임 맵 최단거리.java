import java.util.*;

class Solution {
    
    int[] dx = {1, 0, -1, 0};
    int[] dy = {0, 1, 0, -1};
    
    public int solution(int[][] maps) {
        int answer = 0;
        
        answer = bfs(maps);
        
        return answer;
    }
    
    public int bfs(int[][] maps){
        // 최소 이동 횟수
        int cnt = 1;
        // map의 좌우 길이 구해놓기
        int n = maps.length;
        int m = maps[0].length;
        
        // visited 설정
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;
        
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, 0});
        
        while (!q.isEmpty()) {    
            int size = q.size();
            
            for (int i=0; i<size; i++){
                int[] cur = q.poll();
                int cx = cur[0];
                int cy = cur[1];
                
                if (cx == n - 1 && cy == m - 1) return cnt;
                
                for (int j=0; j<4; j++){
                    int nx = cx + dx[j];
                    int ny = cy + dy[j];
                    
                    // 범위안의 움직임 체크
                    if (nx<0 || nx>=n || ny<0 || ny>=m) continue;
                    // 방문했던곳인지 체크
                    if (visited[nx][ny]) continue;
                    // 벽인지 체크
                    if (maps[nx][ny] == 0) continue;
                    
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx, ny});
                }
            }
            
            // 이동 횟수 증가
            cnt++;
        }
        
        // q가 비울떄 까지 찾지못했으므로 -1을 출력
        return -1;
    }
}