package pb;

import java.util.*;
public class N13565 {
	static class Dot{
		int x, y;
		public Dot(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	static public boolean BFS(int[][] arr, int m, int n) {
		int[][] check = new int[m][n];
		Queue<Dot> q = new LinkedList<>();
		for(int i=0; i<m; i++) {
			for(int j=0; j<n; j++) {
				if(i == 0 && arr[i][j] == 0) {
					check[i][j] = -1;
				}
				else {
					check[i][j] = arr[i][j];
				}
				if(check[i][j] == -1) {
					q.offer(new Dot(i, j));
				}
			}
		}
		while(!q.isEmpty()) {
			Dot tmpD = q.poll();
			int[] dx = {-1,1,0,0};
			int[] dy = {0,0,-1,1};
			for(int i=0; i<4; i++) {
				int nX = tmpD.x + dx[i];
				int nY = tmpD.y + dy[i];
				if(nX<0 || nY<0 || nX>=m || nY>=n) {  
					continue;
				}
				if(check[nX][nY] == 0) {
					check[nX][nY] = -1;
					q.offer(new Dot(nX, nY));
				}
			}
		}
		
		for(int i=0; i<n; i++) {
			if(check[m - 1][i] == -1) {
				return true;
			}
		}
		return false;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int m = sc.nextInt();
		int n = sc.nextInt();
		sc.nextLine();
		int[][] arr = new int[m][n];
		for(int i=0; i<m; i++) {
			String line = sc.nextLine();
			for(int j=0; j<n; j++) {
				arr[i][j] = line.charAt(j) - '0';
			}
		}
		if(BFS(arr, m, n) == true) {
			System.out.println("YES");
		}
		else {
			System.out.println("NO");
		}
		sc.close();
	}
}
