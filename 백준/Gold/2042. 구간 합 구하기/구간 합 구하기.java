import java.io.*;
import java.util.*;


public class Main {
	
	static long[] arr;
	static int N;
	static int B;
	static long [] bucketSum;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		arr = new long[N];
		B = (int) Math.sqrt(N);
		
		for(int i=0; i<N; i++) {
			arr[i] = Long.parseLong(br.readLine().trim());
		}
		
		int bucketCnt = (N-1)/B+1;
		bucketSum = new long[bucketCnt];
		
		// bucket의 구간별 합을 미리 구해둠
		for(int i=0; i<N; i++) {
			bucketSum[i/B] += arr[i];
		}
		
		
		for(int i=0; i<M+K; i++) {
			st = new StringTokenizer(br.readLine());
			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			long c = Long.parseLong(st.nextToken());
			
			// a = 1 -> b번째수를 c로 바꾸기.
			if(a == 1) {
				long delta = c-arr[b-1];
				arr[b-1] = c;
				bucketSum[(b-1)/B] += delta; 
			} else { // a = 2 -> b번째수부터 c번째 수까지의 합 구하기
				System.out.println(bucket(b, (int) c));
			}
		}
	}
	
	static long bucket(int start, int end) {
		// 인덱스 맞춰주기
		start = start-1;
		end = end-1;
		 
		int startBucket = start/B;
		int endBucket = end/B;
		
		long sum = 0;
		
		
		// 1. start를 포함하는 구간합
		if (endBucket - startBucket == 0) {
			// 넘어감
		} else {
			for(int i=start; i<(startBucket+1)*B; i++) {
				sum += arr[i];
			}
		}
		
		// 2. 범위를 완전 포함하는 구간합
		if (endBucket - startBucket <=1) {
			// 넘어감
		} else {
			for(int i=startBucket+1; i<endBucket; i++) {
				sum += bucketSum[i];
			}
		}
		
		// 3. end를 포함하는 구간합
		if (endBucket - startBucket == 0) {
			for(int i=start; i<=end; i++) {
				sum += arr[i];
			}
		} else {
			for(int i=endBucket*B; i<=end; i++) {
				sum += arr[i];
			}
		}
		
		return sum;
	}	
}
