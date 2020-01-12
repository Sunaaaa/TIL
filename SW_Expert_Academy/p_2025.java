// package lv_1;
/*
    SW Expert Academy 2025. N줄 덧셈
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QFZtaAscDFAUq&categoryId=AV5QFZtaAscDFAUq&categoryType=CODE&&&
*/
import java.util.Scanner;

public class p_2025 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		int sum = 0;
		for (int i = 1; i <= test; i++) {
			sum+=i;
		}
		System.out.println(sum);
	}
}
