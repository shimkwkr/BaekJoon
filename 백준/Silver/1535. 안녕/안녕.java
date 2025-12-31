import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] L = new int[N];
        int[] J = new int[N];

        for (int i = 0; i < N; i++) {
            L[i] = sc.nextInt();
        }

        for (int i = 0; i < N; i++) {
            J[i] = sc.nextInt();
        }

        // dp[h] = 체력을 h만큼 사용했을 때 얻을 수 있는 최대 기쁨
        int[] dp = new int[101];

        for (int i = 0; i < N; i++) {
            // 뒤에서부터 갱신 (0/1 배낭)
            for (int h = 100; h >= L[i]; h--) {
                dp[h] = Math.max(dp[h], dp[h - L[i]] + J[i]);
            }
        }

        int answer = 0;
        // 체력 100을 모두 쓰면 죽음 → 99까지만 가능
        for (int h = 1; h < 100; h++) {
            answer = Math.max(answer, dp[h]);
        }

        System.out.println(answer);
    }
}
