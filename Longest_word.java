// author		: babang/DreamHunter
// date			: 10 january 2016
// desc			: program that determines the longest word in a sentence.

import java.io.*;

public class Main {

    public static void _show (String line) {
        String temp[] = line.split(" ");
        int idx = 0;
        int max = temp[0].length();
        for (int i = 1; i < temp.length; i++) {
            if (temp[i].length() > max) {
                idx = i;
                max = temp[i].length();
            }
        }
        System.out.println(temp[idx]);
    }

    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;

        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            // Process line of input Here
            // System.out.println(line);
            _show(line);
        }
    }
}
