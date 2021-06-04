package pb;

import java.util.*;
public class N10026 {
	static class Location {
		public int x;
		public int y;
		
		public Location(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	public static void BFS(char[][] board, int x, int y, boolean[][] visited) {
		Queue<Location> queue = new LinkedList<>();
		
		queue.offer(new Location(x, y));
		char cur_color = board[x][y];
		
		board[x][y] = 'T';
		visited[x][y] = true;
		
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		
		while(!queue.isEmpty()) {
			Location tmp = queue.poll();
			
			for(int i = 0; i < 4; i++) {
				int nx = tmp.x + dx[i];
				int ny = tmp.y + dy[i];
				
				if(nx < 0 || ny < 0 || nx >= board.length || ny >= board.length) {
					continue;
				}
				if(board[nx][ny] == cur_color && !visited[nx][ny]) {
					board[nx][ny] = 'T';
					visited[nx][ny] = true;
					queue.offer(new Location(nx, ny)); 
				}
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = Integer.parseInt(sc.nextLine());
		
		char[][] rgb_colored = new char[n][n];
		char[][] odd_colored = new char[n][n];
		
		for(int i = 0; i < n; i++) {
			String line = sc.nextLine();
			for(int j = 0; j < n; j++) {
				rgb_colored[i][j] = line.charAt(j);
				if(line.charAt(j) == 'G') {
					odd_colored[i][j] = 'R';
				}
				else {
					odd_colored[i][j] = line.charAt(j);
				}
			}
		}
		
		boolean[][] rgb_visited = new boolean[n][n];
		int cnt_rgb = 0;
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				if(rgb_colored[i][j] != 'T' && !rgb_visited[i][j]) {
					cnt_rgb++;
					BFS(rgb_colored, i, j, rgb_visited);
				}
			}
		}
		
		boolean[][] odd_visited = new boolean[n][n];
		int cnt_odd = 0;
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				if(odd_colored[i][j] != 'T' && !odd_visited[i][j]) {
					cnt_odd++;
					BFS(odd_colored, i, j, odd_visited);
				}
			}
		}
		System.out.println(cnt_rgb + " " + cnt_odd);
		
		sc.close();
	}
}
