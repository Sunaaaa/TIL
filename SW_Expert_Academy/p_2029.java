// package lv_1;
/*
    SW Expert Academy 2029. 몫과 나머지 출력하기
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QGNvKAtEDFAUq&categoryId=AV5QGNvKAtEDFAUq&categoryType=CODE
*/
import java.util.Scanner;

public class p_2029 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		int count = 0;
		while (count < test) {
			int a = sc.nextInt(), b = sc.nextInt();
			System.out.println("#"+(count+1)+" "+(a/b)+" "+(a%b));	
			count++;
		}	
	}
}
