package pb;

import java.util.*;
public class N1012 {
	static class Cabbage {
		public int x;
		public int y;
		
		public Cabbage(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	public static void DFS(int[][] soil, int m, int n) {
		Set<Integer> warm = new HashSet<>();
		Stack<Cabbage> farm = new Stack<>();	
		boolean visited[][] = new boolean[n][m];
		
		int cnt = 1;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(soil[i][j] == 1) {
					soil[i][j] = cnt;
					farm.push(new Cabbage(j, i));
				}
				cnt++;
			}
		}
		
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		
		while(!farm.isEmpty()) {
			Cabbage o = farm.pop();
			int visited_x = o.x;
			int visited_y = o.y;
			
			visited[visited_y][visited_x] = true;
			
			for(int i = 0; i < 4; i++) {
				int nX = visited_x + dx[i];
				int nY = visited_y + dy[i];

				if(nX < 0 || nY < 0 || nX >= m || nY >= n) {  
					continue;
				}
				if(soil[nY][nX] != 0 && visited[nY][nX] == false) {
					soil[nY][nX] = soil[visited_y][visited_x];
					visited[nY][nX] = true;
					farm.push(new Cabbage(nX, nY));
				}
			}
		}
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(soil[i][j] != 0) {
					warm.add(soil[i][j]);
				}
			}
		}
		System.out.println(warm.size());
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		
		for(int i = 0; i < t; i++) {
			int m = sc.nextInt();
			int n = sc.nextInt();
			int k = sc.nextInt();
			
			int[][] soil = new int[n][m];
			
			for(int j = 0; j < k; j++) {
				int x = sc.nextInt();
				int y = sc.nextInt();
				
				soil[y][x] = 1;
			}
			DFS(soil, m, n);
		}
		sc.close();
	}
}
