import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] a = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			a[i] = Integer.parseInt(st.nextToken());
		}
		
		// 버킷 크기
		int B =  (int)Math.sqrt(N);
		
		// 전체 버킷의 개수
		int bucketCnt = (N+B-1)/B;
		
		// 버캣 구간합을 저장해놓을 배열
		long[] bucketSum = new long[bucketCnt]; 
		
		// 버캣의 합을 미리 저장
		for(int i=0; i<N; i++) {
			int b = i/B;
			bucketSum[b] += a[i];
		}
		
		
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());;
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			
			// start가 포함된 bucket인덱스
			int bucketStart = (start-1)/B;
			// end가 포함된 bucket인덱스
			int bucketEnd = (end-1)/B;
			
			// 총합
			long sum = 0L;
			
			// 1) 버킷의 시작점 부분의 구간합 구하기
			if (bucketEnd-bucketStart == 0) {
				
			} else {
				for(int j=start-1; j<(bucketStart+1)*B; j++) {
					sum += a[j];
				} 				
			}
			// 2) 완전히 포함되는 버킷은 통채로 더하기
			if (bucketEnd-bucketStart == 0 || bucketEnd-bucketStart == 1) {
				
			} else {
				for(int j=bucketStart+1; j<bucketEnd; j++) {
					sum += bucketSum[j];
				}
			}

			// 3) 남은 꼬리 원소 개별 더하기
			if (bucketEnd-bucketStart == 0) {
				for(int j=start-1; j<end ;j++) {
					sum += a[j];
				}
				
			} else {		
				for(int j=bucketEnd*B; j<end ;j++) {
					sum += a[j];
				}
			}

			System.out.println(sum);
		}
	}
}
