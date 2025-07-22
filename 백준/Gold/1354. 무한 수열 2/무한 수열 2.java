import java.io.*;
import java.util.*;

public class Main {
	
	static Map<Long, Long> map = new HashMap<>();
	static long N;
	static long P;
	static long Q;
	static long X;
	static long Y;
	
	public static void main (String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Long.parseLong(st.nextToken());
		P = Long.parseLong(st.nextToken());
		Q = Long.parseLong(st.nextToken());
		X = Long.parseLong(st.nextToken());
		Y = Long.parseLong(st.nextToken());
		
		long ans = solve(N);
		System.out.println(ans);
	}
	
	
	public static long solve(long n) {
		if (n<=0) return 1;
		
		if (map.containsKey(n)) return map.get(n);
		
		long val = solve(n/P - X) + solve(n/Q - Y);
		
		map.put(n, val);
		
		return val;
	}
}
