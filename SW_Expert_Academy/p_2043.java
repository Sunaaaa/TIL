// package lv_1;
/*
    SW Expert Academy 2043. 서랍의 비밀번호
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QJ_8KAx8DFAUq&categoryId=AV5QJ_8KAx8DFAUq&categoryType=CODE
*/
import java.util.Scanner;

public class p_2043 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int p = sc.nextInt(), k = sc.nextInt(), count = 0;
		
		for (int i = k; i <= 999; i++) {
			count++;
			if (i==p) {
				break;
			}
		}
		System.out.println(count);
		
	}
}
