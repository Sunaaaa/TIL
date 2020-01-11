// package lv_1;
/*
    SW Expert Academy 2063. 중간 값 찾기
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QPsXKA2UDFAUq&categoryId=AV5QPsXKA2UDFAUq&categoryType=CODE
*/
import java.util.Arrays;
import java.util.Scanner;

public class p_2063 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		int num_array[] = new int[test];
		
		for (int i = 0; i < num_array.length; i++) {
			num_array[i] = sc.nextInt();
		}
//		System.out.println(num_array[1]);
		Arrays.sort(num_array);
		System.out.println(num_array[(test/2)]);
		
	}
}
