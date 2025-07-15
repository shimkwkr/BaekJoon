import java.io.*;
import java.util.*;

public class Main {
	
	static int[] arr;
	static int[] lis;
	static int cnt = 0;
	
	public static void main (String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int n = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		
		arr = new int[n+1];
		lis = new int[n+2];
		int len = 1;
		int idx = 1;
		
		for(int i=1; i<=n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			if(arr[i] > lis[len]) {
				len++;
				lis[len]=arr[i];
			} else {
				idx = bin_srch(1, len, arr[i]);
				lis[idx] = arr[i];
			}
		}
		System.out.println(len-1);
	}

	public static int bin_srch(int start, int end, int target) {
		int mid = 0;
		while (start < end) {
			mid = (start+end)/2;
			if(lis[mid] < target) {
				start = mid+1;
			} else {
				end = mid;
			}
		}
		return end;
	}
}
