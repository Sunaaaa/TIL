// package lv_1;
/*
    SW Expert Academy 2050. 알파벳을 숫자로 변환
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QLGxKAzQDFAUq&categoryId=AV5QLGxKAzQDFAUq&categoryType=CODE
*/
import java.util.Scanner;

public class p_2050 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String data = sc.next();
		
		for (int i = 0; i < data.length(); i++) {
			System.out.print(data.charAt(i)-64+" ");
		}
		
	}
}
