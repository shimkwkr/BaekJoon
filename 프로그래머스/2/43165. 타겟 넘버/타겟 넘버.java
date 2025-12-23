class Solution {
    int res = 0;
    
    public int solution(int[] numbers, int target) {
        
        dfs(numbers, target, 0, 0);
        
        return res;
    }
    
    public void dfs(int[] numbers, int target, int n, int sum){
        
        // 기저 조건
        // n이 numbers 길이와 같이지고
        if (n == numbers.length){
            // sum 이 target과 같다면
            if (sum == target){
                ++res;
            }
            return;
        }
        
        // + 선택
        dfs(numbers, target, n+1, sum + numbers[n]);
        // - 선택
        dfs(numbers, target, n+1, sum - numbers[n]);
        
    }
}