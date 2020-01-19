// package lv_2;
/*
    SW Expert Academy 1984. 중간 평균값 구하기
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pw_-KAdcDFAUq&categoryId=AV5Pw_-KAdcDFAUq&categoryType=CODE
*/

import java.util.Arrays;
import java.util.Scanner;

public class p_1984 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		int numbers[] = new int[10];
		for (int i = 0; i < test; i++) {
			int sum = 0;
			
			// numbers 배열에 10개 입력받기 
			for (int j = 0; j < numbers.length; j++) {
				numbers[j] = sc.nextInt();
			}
			Arrays.sort(numbers);
			for (int j = 1; j < numbers.length-1; j++) {
				sum += numbers[j];
			}
			System.out.println("#"+(i+1)+" " + sum/(numbers.length-2));
		}
	}
}
