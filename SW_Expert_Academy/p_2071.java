// package lv_1;
/*
    SW Expert Academy 2071. 평균값 구하기
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE
*/

import java.util.Scanner;

public class p_2071 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int count = 0;
		float sum;
		int test = sc.nextInt();
		int avg_array[] = new int[test];
		while(count < test) {
			sum = 0.0f;
			for (int i = 0; i < 10; i++) {
				sum+=sc.nextInt();				
			}
			avg_array[count] = Math.round(sum/10);
			count++;				
		}
		for (int i = 0; i < avg_array.length; i++) {
			System.out.println("#"+(i+1)+" "+avg_array[i]);
		}
	}
}
