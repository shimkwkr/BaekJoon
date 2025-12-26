import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {};
        
        PriorityQueue<Integer> minhp = new PriorityQueue<>();
        PriorityQueue<Integer> maxhp = new PriorityQueue<>(Comparator.reverseOrder());
        
        Map<Integer, Integer> map = new HashMap<>();
        
        int cnt = 0;
        
        for (int i=0; i<operations.length; i++) {
            // 최댓값 삭제
            if(operations[i].equals("D 1")) {
                if (cnt <= 0) continue;
                
                while(!maxhp.isEmpty() && !map.containsKey(maxhp.peek())){
                    maxhp.poll();
                }
                
                int deleted_key = maxhp.poll();
                map.put(deleted_key, map.get(deleted_key) - 1);
                if(map.get(deleted_key) == 0) map.remove(deleted_key);
                
                cnt--;
                
            } else if (operations[i].equals("D -1")) { // 최솟값 삭제
                if (cnt <= 0) continue;
                
                while(!minhp.isEmpty() && !map.containsKey(minhp.peek())){
                    minhp.poll();
                }
                
                int deleted_key = minhp.poll();
                map.put(deleted_key, map.get(deleted_key) - 1);
                if(map.get(deleted_key) == 0) map.remove(deleted_key);
                
                cnt--;
                
            } else { // 숫자 입력
                int num = Integer.parseInt(operations[i].substring(2));
                map.put(num, map.getOrDefault(num, 0) + 1);
                minhp.offer(num);
                maxhp.offer(num);
                cnt++;
            }
        }
        
        if (cnt >= 2){
            while (!maxhp.isEmpty() && !map.containsKey(maxhp.peek())) {
                maxhp.poll();
            }
            while (!minhp.isEmpty() && !map.containsKey(minhp.peek())) {
                minhp.poll();
            }
            
            answer = new int[] {maxhp.poll(), minhp.poll()};
        } else if (cnt == 1){
            int ansNum = map.keySet().iterator().next();
            answer = new int[] {ansNum, ansNum};
        } else {
            answer = new int[] {0, 0};
        }
        
        return answer;
    }
}