package pb;

import java.util.*;
public class N11724 {
	static boolean[] visited = new boolean[1001];
	
	public static void DFS(int[][] map, int start) {		
		Stack<Integer> stack = new Stack<>();
		
		stack.push(start);
		visited[start] = true;
		
		while(!stack.isEmpty()) {
			int tmp = stack.peek();
			boolean check = false;
			
			for(int i = 1; i < map.length; i++) {
				if(map[tmp][i] == 1 && !visited[i]) {
					visited[i] = true;
					stack.push(i);
					check = true;
					
					break;
				}
			}
			
			if(!check) {
				stack.pop();
			}
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int[][] map = new int[n + 1][n + 1];
		
		for(int i = 0; i < m; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			
			map[u][v] = 1;
			map[v][u] = 1;
		}
		
		int cnt = 0;
		
		for(int i = 1; i < n + 1; i++) {
			if(!visited[i]) {
				cnt++;
				DFS(map, i);
			}
		}
		
		System.out.println(cnt);
		
		sc.close();
	}
}
