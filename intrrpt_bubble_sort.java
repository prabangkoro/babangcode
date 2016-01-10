// author		: babang/DreamHunter
// date			: 10 january 2016
// desc			: program that determines sorting result of data.

import java.io.*;

public class Main {

    public static void _sort (String line) {
        String temp[] = line.split(" ");
        int[] nums = new int[temp.length-2];
        for (int i = 0; i < temp.length-2; i++) {
            nums[i] = Integer.parseInt(temp[i]);
        }
        int i, k;
        for (i = 0; i < Integer.parseInt(temp[temp.length-1]); i++) {
            for (k = 0; k < nums.length-i-1; k++) {
                if (nums[k] > nums[k+1]) {
                    int _temp;
                    _temp = nums[k];
                    nums[k] = nums[k+1];
                    nums[k+1] = _temp;
                }
            }
        }

        for (i = 0; i < nums.length; i++) {
            if (i != nums.length-1){
                System.out.print(nums[i]);
                System.out.print(" ");
            } else {
                System.out.println(nums[i]);
            }
            
        }
    }

    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;

        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            _sort(line);
        }
    }
}
