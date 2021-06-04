package pb;

import java.util.*;
public class N2583 {
	static class Dot{
		public int x;
		public int y;
		
		public Dot(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int m = sc.nextInt();
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		int[][] board = new int[m][n];
		
		for(int i = 0; i < k; i++) {
			int l_x = sc.nextInt();
			int l_y = sc.nextInt();
			int r_x = sc.nextInt();
			int r_y = sc.nextInt();
			
			for(int j = l_y; j < r_y; j++) {
				for(int p = l_x; p < r_x; p++) {
					board[j][p] = 1;
				}
			}
		}
		
		Stack<Dot> stack = new Stack<>();
		boolean[][] visited = new boolean[m][n];
		
		int loc = 1;
		for(int i = 0; i < m; i++) {
			for(int j = 0; j < n; j++) {
				loc++;
				if(board[i][j] == 0) {
					board[i][j] = loc;
					stack.push(new Dot(i, j));
				}
			}
		}
		
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		
		while(!stack.isEmpty()) {
			Dot tmp = stack.peek();
			boolean check = false;
			
			for(int i = 0; i < 4; i++) {
				int nx = tmp.x + dx[i];
				int ny = tmp.y + dy[i];
				
				if(nx < 0 || ny < 0 || nx >= m || ny >= n) {
					continue;
				}
				if(board[nx][ny] != 1 && !visited[nx][ny]) {
					visited[nx][ny] = true;
					check = true;
					board[nx][ny] = board[tmp.x][tmp.y];
					stack.push(new Dot(nx, ny));
					
					break;
				}
			}
			if(!check) {
				stack.pop();
			}
		}
		
		Map<Integer, Integer> result = new HashMap<>();
		
		for(int i = 0; i < m; i++) {
			for(int j = 0; j < n; j++) {
				if(board[i][j] != 1 && !result.containsKey(board[i][j])) {
					result.put(board[i][j], 1);
				}
				else if(board[i][j] != 1 && result.containsKey(board[i][j])) {
					result.put(board[i][j], result.get(board[i][j]) + 1);
				}
			}
		}
		
		List<Integer> list = new ArrayList<>(result.keySet());
		Collections.sort(list, (o1, o2) -> (result.get(o1).compareTo(result.get(o2))));
		
		System.out.println(result.size());
		for(Integer key : list) {
			System.out.print(result.get(key) + " ");
		}
		
		sc.close();
	}
}
