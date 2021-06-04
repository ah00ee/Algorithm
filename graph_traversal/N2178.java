package pb;

import java.util.*;
public class N2178 {
	static class Location{
		public int x;
		public int y;
		public int blocks;
		
		public Location(int x, int y, int blocks) {
			this.x = x;
			this.y = y;
			this.blocks = blocks;
		}
	}
	
	public static int BFS(int[][] maze, int n, int m) {
		Queue<Location> queue = new LinkedList<>();
		boolean[][] visited = new boolean[n][m];
		
		queue.offer(new Location(0, 0, 1));
		visited[0][0] = true;
		
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		
		while(!queue.isEmpty()) {
			Location tmp = queue.poll();
			
			for(int i = 0; i < 4; i++) {
				int nx = tmp.x + dx[i];
				int ny = tmp.y + dy[i];
				
				if(nx < 0 || ny < 0 || nx >= n || ny >= m) {
					continue;
				}
				if(nx == n - 1 && ny == m - 1) {
					return tmp.blocks + 1;
				}
				if(maze[nx][ny] != 0 && !visited[nx][ny]) {
					visited[nx][ny] = true;
					maze[nx][ny] = tmp.blocks + 1;
					queue.offer(new Location(nx, ny, tmp.blocks + 1));
				}
			}
		}
		return -1;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		sc.nextLine();
		
		int[][] maze = new int[n][m];
		
		for(int i = 0; i < n; i++) {
			String[] line = sc.nextLine().split("");
			
			for(int j = 0; j < m; j++) {
				maze[i][j] = Integer.parseInt(line[j]); 
			}
		}
		System.out.println(BFS(maze, n, m));
		sc.close();
	}
}
