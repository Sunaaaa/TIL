// package lv_1;
/*
    SW Expert Academy 2058. 자릿수 더하기
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QPRjqA10DFAUq&categoryId=AV5QPRjqA10DFAUq&categoryType=CODE
*/
import java.util.Scanner;

public class p_2058 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a = String.valueOf(sc.nextInt());
		int sum = 0;
		for (int i = 0; i < a.length(); i++) {
			sum+=Integer.parseInt(String.valueOf(a.charAt(i)));
		}		
		System.out.println(sum);
	}
}
