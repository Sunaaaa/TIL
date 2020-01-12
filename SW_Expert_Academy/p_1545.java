// package lv_1;
/*
    SW Expert Academy 1545. 거꾸로 출력해 보아요
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2gbY0qAAQBBAS0&categoryId=AV2gbY0qAAQBBAS0&categoryType=CODE
*/
import java.util.Scanner;

public class p_1545 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		for (int i = test; i >= 0; i--) {
			System.out.print(i+" ");			
		}
	}
}
