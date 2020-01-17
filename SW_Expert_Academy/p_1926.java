// package lv_2;
/*
    SW Expert Academy 1926. 간단한 369게임
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&&&
*/

package lv_1;

import java.util.Scanner;

public class p_1926 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int count = 0;
		String num_array[] = new String[4];

		for (int i = 1; i <= n; i++) {
			count = 0;
			if (i<=32) {
				if (String.valueOf(i).contains("3")||String.valueOf(i).contains("6")||String.valueOf(i).contains("9")) {
					System.out.print("- ");
				}else System.out.print(i+" ");
				
			} else {
				num_array = String.valueOf(i).split("");
				for (int j = 0; j < num_array.length; j++) {
					if (String.valueOf(i).contains("3")||String.valueOf(i).contains("6")||String.valueOf(i).contains("9")) {
						count++;
					} else continue;
				}
				System.out.println("count는"+count);
				for (int j = 0; j < count; j++) {
					System.out.print("-");
				}
				System.out.print(" ");
			}
		}
		
		
	}
}
