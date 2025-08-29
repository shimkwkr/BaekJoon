import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int N = Integer.parseInt(br.readLine());

    	
    	
    	if (N==1) {
    		br.readLine();
    		System.out.println(0);
    		return;
    	}
    	
    	int dasom = Integer.parseInt(br.readLine());
    	int cnt = 0;
    	PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
    	
    	for (int i=0; i<N-1; i++) {
    		maxHeap.offer(Integer.parseInt(br.readLine()));
    	}
    	
    	while (dasom <= maxHeap.peek()) {
    		int top = maxHeap.poll();
    		cnt++;
    		dasom++;
    		top--;
    		maxHeap.offer(top);
    	}
    	
    	System.out.print(cnt);
    	
    }
}
