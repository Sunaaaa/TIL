// package lv_1;
/*
    SW Expert Academy 2019. 더블더블
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QDEX6AqwDFAUq&categoryId=AV5QDEX6AqwDFAUq&categoryType=CODE
*/
import java.util.Scanner;

public class p_2019 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		int mul=1;
		System.out.print(1+" ");
		for (int i = 1; i <= test; i++) {
			mul*=2;
			System.out.print(mul+" ");
		}
	}
}
