// package lv_3;
/*
    SW Expert Academy 7272. 안경이 없어 
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWl0ZQ8qn7UDFAXz&categoryId=AWl0ZQ8qn7UDFAXz&categoryType=CODE
*/
import java.util.Scanner;

public class p_7272안경이없어 {
	
	static int[] c = {1,2,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int i = 1; i <= T; i++) {
			String str = sc.next();
			String str2 = sc.next();
			boolean flag = true;

			if (str.length() == str2.length()) {
				for (int j = 0; j < str.length(); j++) {
					char a = str.charAt(j);
					char b = str2.charAt(j);
					
					if (c[a-'A']!=c[b-'A']) {
						flag = false;
						break;
					}
					
				}
			} else
				flag = false;

			if (flag == true) {
				System.out.printf("#%d %s\n", i, "SAME");
			} else
				System.out.printf("#%d %s\n", i, "DIFF");

		}
	}
}
