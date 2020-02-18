// package lv_3;
/*
    SW Expert Academy 3314. 보충학습과 평균
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBnA2jaxDsDFAWr&categoryId=AWBnA2jaxDsDFAWr&categoryType=CODE&&&
*/

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class p_3314 {
	static int[] arr;

	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("3314.txt"));
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int tc = 1; tc <= T; tc++) {
			arr = new int[5];

			for (int i = 0; i < 5; i++) {
				int a = sc.nextInt();
				if (a < 40) {
					a = 40;
				}
				arr[i] = a;
			}
			int sum = 0;
			for (int i = 0; i < 5; i++) {
				sum+=arr[i];
			}
			
			System.out.printf("#%d %d\n", tc, sum/5
					);
		}

	}
}
