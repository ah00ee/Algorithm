package pb;

import java.util.*;
public class N4963 {
	static class Island{
		public int x;
		public int y;
		
		public Island(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	static public int DFS(int[][] island, int x, int y) {
		Stack<Island> stack = new Stack<>();
		Set<Integer> result = new HashSet<>();
		boolean[][] visited = new boolean[x][y];
		
		int cnt = 0;
		
		for(int i = 0; i < x; i++) {
			for(int j = 0; j < y; j++) {
				cnt++;
				
				if(island[i][j] != 0) {
					island[i][j] = cnt;
					stack.push(new Island(i, j));
					visited[i][j] = true;
				}
			}
		}
		
		int[] dx = {-1, -1, -1, 1, 1, 1, 0, 0};
		int[] dy = {0, -1, 1, 0, -1, 1, -1, 1};
		
		while(!stack.isEmpty()) {
			Island tmp = stack.peek();
			
			boolean check = false;
			for(int i = 0; i < 8; i++) {
				int nx = tmp.x + dx[i];
				int ny = tmp.y + dy[i];
				
				if(nx < 0 || ny < 0 || nx >= x || ny >= y) {
					continue;
				}
				if(visited[nx][ny]) {
					island[nx][ny] = island[tmp.x][tmp.y];
					visited[nx][ny] = false;
					stack.push(new Island(nx, ny));
					check = true;

					break;
				}
			}
			
			if(!check) {
				stack.pop();
			}
		}
		for(int i = 0; i < x; i++) {
			for(int j = 0; j < y; j++) {
				if(island[i][j] != 0) {
					result.add(island[i][j]);
				}
			}
		}
		
		return result.size();
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			int w = sc.nextInt();
			int h = sc.nextInt();
			
			if(w == 0 && h == 0)	break;
			
			int[][] island = new int[h][w];
			for(int i = 0; i < h; i++) {
				for(int j = 0; j < w; j++) {
					island[i][j] = sc.nextInt();
				}
			}
			
			System.out.println(DFS(island, h, w));
		}
		sc.close();
	}
}
