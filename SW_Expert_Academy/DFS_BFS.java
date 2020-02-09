package algo;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class DFS와BFS {
	static int[][] arr;
	static boolean[] visited;

	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("dfsbfs.txt"));
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();
		int V = sc.nextInt();

		arr = new int[N + 1][N + 1];
		visited = new boolean[N+1];
		

		for (int j = 1; j <= M; j++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			arr[a][b] = 1;
			arr[b][a] = 1;
		}
		
		dfs(V);
		System.out.println();
		
		Queue<Integer> queue = new LinkedList<Integer>();
		visited = new boolean[N+1];
		
		queue.offer(V);
		visited[V] = true;
		
		while (!queue.isEmpty()) {
			int a = queue.poll();
			System.out.printf("%d ", a);
			for (int i = 1; i <= N; i++) {
				if (arr[a][i] == 1  && !visited[i]) {
					queue.offer(i);
					visited[i] = true;
				}
			}
		}
		
	}

	private static void dfs(int i) {
		visited[i] = true;
		System.out.printf("%d ", i);
		for (int j = 1; j < arr.length; j++) {
			if (arr[i][j]==1&&visited[j]==false) {
				visited[j] =true;
				dfs(j);
			}
		}
	}
}
