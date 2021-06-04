package pb;

import java.util.*;
public class N1260 {
	public static void DFS(int[][] map, int v) {
		Stack<Integer> dfs = new Stack<>();
		
		boolean visited[] = new boolean[map.length];

		dfs.push(v);
		visited[v] = true;
		System.out.print(v + " ");
		
		while(!dfs.isEmpty()) {
			int tmpDot = dfs.peek();
			boolean flag = false;
			
			for(int i = 1; i < map.length; i++) {
				if(map[tmpDot][i] == 1 && !visited[i]) {
					dfs.push(i);
					visited[i] = true;
					System.out.print(i + " ");
					flag = true;
					
					break;
				}
			}
			
			if(!flag) {
				dfs.pop();
			}
		}
	}
	
	public static void BFS(int[][] map, int v) {
		Queue<Integer> bfs = new LinkedList<>();
		
		boolean visited[] = new boolean[map.length];
		bfs.offer(v);
		visited[v] = true;
		System.out.print(v + " ");
		
		while(!bfs.isEmpty()) {
			int tmpDot = bfs.poll();
			
			for(int i = 1; i < map.length; i++) {
				if(map[tmpDot][i] == 1 && !visited[i]) {
					bfs.offer(i);
					visited[i] = true;
					System.out.print(i + " ");
				}
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		int v = sc.nextInt();
		
		int[][] map = new int[n + 1][n + 1];
		
		for(int i = 0; i < m; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			map[x][y] = 1;
			map[y][x] = 1;
		}
		
		DFS(map, v);
		System.out.println();
		BFS(map, v);
		
		sc.close();
	}
}
