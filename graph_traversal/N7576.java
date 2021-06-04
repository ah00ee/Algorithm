package pb;

import java.util.*;
public class N7576 {
	static class Dot{
		int x, y;
		public Dot(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	public static void Search(int[][] arr, int n, int m) {
		Queue<Dot> tomato = new LinkedList<Dot>();
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(arr[i][j] == 1) {    
					tomato.offer(new Dot(i, j));
				}
			}
		}
		
		int cnt = tomato.size(), day = 0;
		
		while(!tomato.isEmpty()) { 
			
			if(cnt == 0) {
				day++;
				cnt = tomato.size();
			}
			
			Dot d = tomato.poll();
			int[] dx = {-1,1,0,0};
			int[] dy = {0,0,-1,1};
			
			for(int i=0; i<4; i++) {
				int nX = d.x + dx[i];
				int nY = d.y + dy[i];
				
				if(nX<0 || nY<0 || nX>=n || nY>=m) {  
					continue;
				}
				if(arr[nX][nY] == 0) {
					arr[nX][nY] = 1;
					tomato.offer(new Dot(nX, nY));
				}
			}
			cnt--;
		}
		
		boolean out = false;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(arr[i][j] == 0) {
					System.out.println(-1);
					out = true;
					
					break;
				}
			}
			if(out)	break;
		}
		
		if(!out) {
			System.out.println(day);
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int m = sc.nextInt();
		int n = sc.nextInt();
		
		int[][] arr = new int[n][m];
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		Search(arr, n, m);
		
		sc.close();
	}
}