import java.io.*;
import java.util.*;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int[] count = new int[20];
		int[] names = new int[N];
		
		for(int i=0; i<N; i++) {
			int num = Integer.parseInt(br.readLine());
			names[i] = num;
			
			for (int j=0; j<20; j++) {
				if((num & (1 << j)) != 0) {
					count[j]++;
				}
			}
		}
		
		long ans = 0;
		
		if (N == 1) {
			System.out.println(names[0]);
		} else {
			for(int i=0; i<20; i++) {
				int ones = count[i];
				int zeros = N - ones;
				ans += (long) ones * zeros * (1L << i);
			}
			
			System.out.println(ans);			
		}
	}
}
