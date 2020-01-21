// package lv_2;
/*
    SW Expert Academy 1966. 숫자를 정렬하자
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PrmyKAWEDFAUq&categoryId=AV5PrmyKAWEDFAUq&categoryType=CODE
*/

import java.util.Arrays;
import java.util.Scanner;

public class p_1966 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int test = sc.nextInt();
		for (int i = 1; i < test+1; i++) {
			int n = sc.nextInt();
			int[] arr = new int[n];
			
			for (int j = 0; j < arr.length; j++) {
				arr[j] = sc.nextInt();
			}
			Arrays.sort(arr);
			System.out.print("#"+i+" ");
			for (int j = 0; j < arr.length; j++) {
				System.out.print(arr[j]+" ");
			}
			
		}
		
	}
}
