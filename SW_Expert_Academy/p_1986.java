// package lv_2;
/*
    SW Expert Academy 1986. 지그재그 숫자
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PxmBqAe8DFAUq&categoryId=AV5PxmBqAe8DFAUq&categoryType=CODE
*/

import java.util.Scanner;

public class p_1986 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		int count = 0;
		while (count < test) {
			int sum = 1;
			int n = sc.nextInt();
			for (int i = 2; i <= n; i++) {
				if (i%2==0) {
					sum-=i;
				} else {
					sum+=i;
				}
			}
			System.out.println("#"+(count+1)+" "+sum);
		}
	}
}
