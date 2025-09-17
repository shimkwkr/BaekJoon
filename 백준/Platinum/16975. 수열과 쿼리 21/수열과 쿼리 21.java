import java.io.*;
import java.util.*;

public class Main {
	
	// k값에 따른 버킷의 변동 정보
	static long[] bucketSumInfo;
	static long[] arr;
	static int N;
	static int B;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		B = (int) Math.sqrt(N);
		bucketSumInfo = new long[(N-1)/B + 1];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		arr = new long[N];
		for(int i=0; i<N; i++) {
			arr[i]= Integer.parseInt(st.nextToken());
		}
		
		int M = Integer.parseInt(br.readLine());
		
		
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			
			// 1 인 경우 Ai ~ Aj 에 k를 더한다
			if (Integer.parseInt(st.nextToken()) == 1) {
				int start = Integer.parseInt(st.nextToken());
				int end = Integer.parseInt(st.nextToken());
				int k = Integer.parseInt(st.nextToken());
				
				bucket(start, end, k);
				
			} else { // 2 인 경우 Ax를 출력한다.
				int x = Integer.parseInt(st.nextToken());
				System.out.println(arr[x-1] + bucketSumInfo[(x-1)/B]);
			}
		}
	}
	
	static void bucket(int start, int end, int k) {
		start = start-1;
		end = end-1;
		
		int startBucket = start/B; 
		int endBucket = end/B;
		
		// 1. 시작지점 버킷 확인
		if(endBucket-startBucket == 0) {
			// 넘어감
		} else {
			for(int i=start; i<(startBucket+1)*B;i++) {
				arr[i]+=k;
			}
		}
		
		// 2. 구간을 모두 포함하는 버킷 확인
		if(endBucket-startBucket <= 1) {
			// 넘어감
		} else {
			// k값에 따른 버킷의 변동 정보 입력
			for(int i=startBucket+1; i<endBucket; i++) {
				bucketSumInfo[i] += k;
			}
		}
		
		// 3. 마지막지점 버킷 확인
		if(endBucket-startBucket == 0) {
			for(int i=start; i<=end;i++) {
				arr[i]+=k;
			}
		} else {
			for(int i=endBucket*B; i<=end;i++) {
				arr[i]+=k;
			}
		}
		
	}
}
