import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int cnt = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int score : scoville){
            pq.offer(score);
        }
        
        while (true) {
            int score = pq.poll();
            if (score < K) {
                if(pq.size() > 0){
                    int nxt_score = pq.poll();
                    pq.offer(score + nxt_score*2);
                    cnt++;        
                } else {
                    return -1;  
                }
            } else {
                break;
            }
        }
        
        return cnt;
    }
}