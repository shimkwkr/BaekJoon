import java.io.*;
import java.util.*;

public class Main {
    static int MAX = 1_000_001;
    static int[] next = new int[MAX];
    static int[] prev = new int[MAX];
    static boolean[] exist = new boolean[MAX];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] stations = new int[N];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            stations[i] = Integer.parseInt(st.nextToken());
            exist[stations[i]] = true;
        }

        // 연결 리스트 구성
        for (int i = 0; i < N; i++) {
            int cur = stations[i];
            int p = stations[(i - 1 + N) % N];
            int n = stations[(i + 1) % N];
            prev[cur] = p;
            next[cur] = n;
        }

        for (int t = 0; t < M; t++) {
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            int i = Integer.parseInt(st.nextToken());

            if (cmd.equals("BN")) {
                int j = Integer.parseInt(st.nextToken());
                int ni = next[i];
                bw.write(ni + "\n");

                // insert j between i and ni
                next[i] = j;
                prev[ni] = j;
                next[j] = ni;
                prev[j] = i;
                exist[j] = true;

            } else if (cmd.equals("BP")) {
                int j = Integer.parseInt(st.nextToken());
                int pi = prev[i];
                bw.write(pi + "\n");

                // insert j between pi and i
                next[pi] = j;
                prev[i] = j;
                next[j] = i;
                prev[j] = pi;
                exist[j] = true;

            } else if (cmd.equals("CN")) {
                int ni = next[i];
                int nni = next[ni];
                bw.write(ni + "\n");

                // delete ni
                next[i] = nni;
                prev[nni] = i;
                exist[ni] = false;

            } else if (cmd.equals("CP")) {
                int pi = prev[i];
                int ppi = prev[pi];
                bw.write(pi + "\n");

                // delete pi
                prev[i] = ppi;
                next[ppi] = i;
                exist[pi] = false;
            }
        }

        bw.flush();
        bw.close();
    }
}
