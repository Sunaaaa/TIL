// package lv_2;
/*
    SW Expert Academy 2005. 파스칼의 삼각형
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE
*/
package lv_2;

import java.util.Scanner;

public class p_2005 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		int	max = 0, num = 0;
		for (int i = 0; i < test; i++) {
			max++;
			System.out.print("1" + " ");
			for (int j = 0; j < i-1; j++) {
				System.out.print(max + " ");
			}
			System.out.print("1" + " ");
			System.out.println("");
		}
	}
}
