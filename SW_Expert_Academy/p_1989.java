// package lv_2;
/*
    SW Expert Academy 1989. 초심자의 회문 검사
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PyTLqAf4DFAUq&categoryId=AV5PyTLqAf4DFAUq&categoryType=CODE
*/

import java.util.Scanner;

public class p_1989 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.next();
		
		int result = 1;
		
		for (int i = 0, j = str.length()-1; i!=j; i++, j--) {
			char a = str.charAt(i);
			char b = str.charAt(j);
			
			if (a!=b) {
				result = 0;
				break;
			}
		}
		
		System.out.println(result);
		
	}

}
