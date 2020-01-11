// package lv_1;
/*
    SW Expert Academy 2070. 큰 놈, 작은 놈, 같은 놈
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE&&&
*/

import java.util.Scanner;

public class p_2070 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		int count = 0;
		
		for (int i = 0; i < test; i++) {
			long a = sc.nextLong();
			long b = sc.nextLong();
			if (a==b) {
				System.out.println("#"+(i+1)+" =");
			} else if (a>b) {
				System.out.println("#"+(i+1)+" >");
			} else {
				System.out.println("#"+(i+1)+" <");
			}
		}
	}
}
