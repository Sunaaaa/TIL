// package lv_1;
/*
    SW Expert Academy 2068. 최대 수 구하기
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE
*/
import java.util.Scanner;

public class p_2068 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		int count = 0, max, num;
		int max_array[] = new int[test];
		while (count < test) {
			max = 0;
			for (int i = 0; i < 10; i++) {
				num = sc.nextInt();
				if (num > max) {
					max = num;
				}
			}
			max_array[count] = max;
			count++;
		}
		for (int i=0; i < max_array.length; i++) {
			System.out.println("#"+(i+1)+" "+max_array[i]);
		}
	}
}
