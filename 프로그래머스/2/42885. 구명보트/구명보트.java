import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        int left = 0;
        int right = people.length-1;
        int twoRide = 0;
        
        Arrays.sort(people);
        
        while (left<right){
            int sum = 0;
            
            if (people[left] + people[right]  <= limit){
                left++;
                right--;
                twoRide++;
            } else {
                right--;
            }
        }
        
        return people.length-twoRide;
    }
}