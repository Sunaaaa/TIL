// package lv_1;
/*
    SW Expert Academy 2056. 연월일 달력
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE
*/
import java.util.Scanner;

public class p_2056 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		int count = 0;
		String result[] = new String[test]; 
		while(count < test) {
			String data = sc.next();
			int month = Integer.parseInt(data.substring(4, 6));
			int day = Integer.parseInt(data.substring(6));
			if (month < 1 || month >12 || day < 1) {
				result[count] = "-1";
			} else {							
				if (month == 4 || month == 6 || month == 9 || month == 11) {
					if (day > 30) result[count] = "-1";						
					else result[count] = data.substring(0, 4) + "/" + data.substring(4, 6) + "/" + data.substring(6); 
				} else if (month == 2) {
					if (day > 28) result[count] = "-1";						
					else result[count] = data.substring(0, 4) + "/" + data.substring(4, 6) + "/" + data.substring(6); 
				} else {
					if (day > 31) result[count] = "-1";						
					else result[count] = data.substring(0, 4) + "/" + data.substring(4, 6) + "/" + data.substring(6); 
				}
			}						
			count++;
		}
		
		for (int i = 0; i < result.length; i++) {
			System.out.println("#"+(i+1)+" "+result[i]);			
		}
	}
}
