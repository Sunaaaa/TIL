// package lv_1;
/*
    SW Expert Academy 1933. 간단한 N의 약수
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PhcWaAKIDFAUq&categoryId=AV5PhcWaAKIDFAUq&categoryType=CODE
*/
import java.util.ArrayList;
import java.util.Scanner;

public class p_1933 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
//		int yaksu_array[] = new int[n/2];
		ArrayList<Integer> yaksu_array = new ArrayList<Integer>();
		for (int i = 1; i <= n/2; i++) {
			if (n%i==0) {
				yaksu_array.add(i);
				int p = yaksu_array.size();
			}
		}
		yaksu_array.add(n);
		yaksu_array.forEach(t->System.out.println(t));
	}
}
