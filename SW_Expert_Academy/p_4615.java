// package lv_3;
/*
    SW Expert Academy 4615. 재미있는 오셀로 게임
    문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQmA4uK8ygDFAXj
*/
import java.util.Arrays;
import java.util.Scanner;

public class p_4615 {
    static char[][] arr;
    static int[][] list;
    static int[] dr = { -1, -1, -1, 0, 1, 1, 1, 0 };
    static int[] dc = { -1, 0, 1, 1, 1, 0, -1, -1 };

    public static void main(final String[] args) {
        final Scanner sc = new Scanner(System.in);

        final int T = sc.nextInt();
        for (final int tc = 1; tc <= T; tc++) {

            final int N = sc.nextInt();
            final int M = sc.nextInt();
            final int wCnt = 0, bCnt = 0;
            arr = new char[N][N];
            list = new int[M][3];

            for (int i = 0; i < arr.length; i++) {
                for (int j = 0; j < arr.length; j++) {
                    arr[i][j] = 'N';
                }
            }

            arr[N / 2][N / 2] = 'W';
            arr[N / 2][N / 2 - 1] = 'B';
            arr[N / 2 - 1][N / 2] = 'B';
            arr[N / 2 - 1][N / 2 - 1] = 'W';

            for (final int i = 0; i < M; i++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                int c = sc.nextInt();
                list[i][0] = c;
                list[i][1] = x - 1;
                list[i][2] = y - 1;
            }
 
            for (final int i = 0; i < M; i++) {
 
                final char me = getStone(list[i][0]);
                final char you = getStone(me);
 
                final int r = list[i][1];
                final int c = list[i][2];
 
                A: for (final int k = 0; k < dr.length; k++) {
                    final int cnt = 0;
                    final int nr = r + dr[k];
                    final int nc = c + dc[k];
 
                    if (nr >= 0 && nc >= 0 && nr < N && nc < N) {
                        if (arr[nr][nc] == 'N' || arr[nr][nc] == me) {
                            continue A;
                        } else {
                            cnt += 1;
 
                            // 범위 안에 들어왔는데 상대방 말이면 거기부터 탐색
                            for (int j = 2; j <= N; j++) {
                                int nnr = r + dr[k] * j;
                                int nnc = c + dc[k] * j;
 
                                if (nnr >= 0 && nnc >= 0 && nnr < N && nnc < N) {
                                    if (arr[nnr][nnc] == 'N') {
                                        // 빈 공간이면 다른 방향으로 돌리기
                                        continue A;
                                    } else if (arr[nnr][nnc] == you) {
                                        cnt += 1;
                                    } else
                                        break;
 
                                } // 다른 방향으로 돌리기
                                else
                                    continue A;
                            }
 
                        }
 
                    } // 다른 방향으로 돌리기
 
                    if (cnt == 0) {
                        arr[r][c] = me;
                        continue A;
                    } else {
                        for (int j = 1; j <= cnt; j++) {
                            int nnr = r + dr[k] * j;
                            int nnc = c + dc[k] * j;
                            arr[nnr][nnc] = me;
                        }
                        arr[r][c] = me;
                    }
                }
            }
 
            // 돌의 갯수 세기
            for (int t = 0; t < N; t++) {
                for (int p = 0; p < N; p++) {
                    if (arr[t][p] == 'W') {
                        wCnt += 1;
                    } else if (arr[t][p] == 'B') {
                        bCnt += 1;
                    }
                }
            }
 
            System.out.printf("#%d %d %d\n", tc, bCnt, wCnt);
        }
    }
 
    static char getStone(final int a) {
        if (a == 1)
            return 'B';
        else
            return 'W';
    }
 
    static char getStone(final char c) {
        if (c == 'B')
            return 'W';
        else
            return 'B';
    }
 
    static void print() {
        for (int i = 0; i < arr.length; i++) {
            System.out.println(Arrays.toString(arr[i]));
        }
        System.out.println("_________________________________");
    }
}