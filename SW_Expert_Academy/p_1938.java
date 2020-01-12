// package lv_1;
/*
    SW Expert Academy 1938. 아주 간단한 계산기
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjsYKAMIDFAUq&categoryId=AV5PjsYKAMIDFAUq&categoryType=CODE
*/
import java.util.Scanner;

public class p_1938 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.println(a+b);
		System.out.println(a-b);
		System.out.println(a*b);
//		System.out.println(Math.floor(a/b));
		System.out.println(a/b);
	}
}
