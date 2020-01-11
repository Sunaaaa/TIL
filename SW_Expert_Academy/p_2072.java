// package lv_1;
/*
    SW Expert Academy 2072. 홀수만 더하기
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq
*/
import java.util.Scanner;


public class p_2072 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		int count = 0;		
		int sum_array[] = new int[test];
		while(count<test) {
			System.out.println(count);
			int number[] = new int[10];
			int sum = 0;
			
			for (int i = 0; i < 10; i++) {
				number[i] = sc.nextInt();
			}

			for (int i : number) {
				if (i%2!=0) {
					sum+=i;
				}
			}			
			sum_array[count]=sum;
			count++;
			
		}		
		for (int i = 0; i < test; i++) {
			System.out.println("#"+i+" " + sum_array[i]);
		}
	}	
}
