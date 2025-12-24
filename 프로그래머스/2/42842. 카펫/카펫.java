import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        
        for(int i=1; i<=(int)Math.sqrt(yellow); i++){
            // yellow의 약수가 아니라면
            if (yellow % i != 0){
                continue;
            } else { // yellow의 약수라면
                // yellow의 세로 길이
                int yellow_col = i;
                //yellow의 가로 길이
                int yellow_row = yellow / i;
                
                // brown 개수 계산
                int cnt_brown = yellow_row*2 + yellow_col*2 + 4;
                
                
                if(cnt_brown ==  brown){
                    answer = new int[] {yellow_row+2, yellow_col+2};
                    break;
                }
            }
        }
        
        
        return answer;
    }
}