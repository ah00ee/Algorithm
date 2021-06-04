package pb;

import java.util.*;
public class N2606 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int computer = sc.nextInt();
		int pair = sc.nextInt();
		
		int[][] map = new int[computer + 1][computer + 1];
		
		for(int i = 0; i < pair; i++) {
			int fir = sc.nextInt();
			int sec = sc.nextInt();
			
			map[fir][sec] = 1;
			map[sec][fir] = 1;
		}
		
		Stack<Integer> stack = new Stack<>();
		boolean visited[] = new boolean[computer + 1];
		
		stack.push(1);
		visited[1] = true;
		
		int cnt = 0;
		
		while(!stack.isEmpty()) {
			int tmp = stack.peek();
			
			boolean check = false;
			
			for(int i = 1; i < computer + 1; i++) {
				if(map[tmp][i] == 1 && !visited[i]) {
					visited[i] = true;
					stack.push(i);
					cnt++;
					
					check = true;
					break;
				}
			}
			
			if(!check) {
				stack.pop();
			}
		}
		
		System.out.println(cnt);
		
		sc.close();
	}
}
