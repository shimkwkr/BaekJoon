import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        // 장르별 총 플레이 횟수 기록용
        Map<String, Integer> mapTotalPlay = new HashMap<>();
        // 장르별 플레이횟수, 고유번호 기록용
        Map<String, PriorityQueue<int[]>> mapInfo = new HashMap<>();
        
        Comparator<Map.Entry<String, Integer>> comp2 = (a, b) -> {
            return b.getValue() - a.getValue(); // 플레이수 기준 내름차순
        };
        
        PriorityQueue<Map.Entry<String, Integer>> pqTotalPlay = new PriorityQueue<>(comp2);
        
        Comparator<int[]> comp1 = (a, b) -> {
            if (a[0] != b[0]) return b[0]-a[0]; // 재생수 기준 내림차순
            return a[1] - b[1]; // 고유번호 기준 오름차순
        };
        
        // 장르별 총 플레이 횟수 구하기
        for (int i=0; i<genres.length; i++) {
            
            mapTotalPlay.put(genres[i], mapTotalPlay.getOrDefault(genres[i], 0) + plays[i]);
            
            mapInfo.putIfAbsent(genres[i], new PriorityQueue<>(comp1));
                
            mapInfo.get(genres[i]).offer(new int[] {plays[i], i});

        }
        
        for (var e : mapTotalPlay.entrySet()){
            pqTotalPlay.offer(e);
        }
        
        while (!pqTotalPlay.isEmpty()) {
            // 현재 최다 플레이 장르
            String gen = pqTotalPlay.poll().getKey();
            
            // 현재 최다 플레이 장르의 곡 정보 힙
            PriorityQueue<int[]> maxGenInfo = mapInfo.get(gen);
            
            // 장르내 속한 곡이 하나라면 하나의 곡만 선택
            if (maxGenInfo.size() == 1){
                answer.add(maxGenInfo.poll()[1]);
            } else { // 속한 곡이 2개이상이라면
                answer.add(maxGenInfo.poll()[1]);
                answer.add(maxGenInfo.poll()[1]);
            }   
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}