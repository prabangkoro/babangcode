// author		: babang/DreamHunter
// date			: 10 january 2016
// desc			: program that determines the memory management system of computer.

import java.nio.ByteOrder;
import java.io.*;

public class Main {
    public static void main (String [] args) throws IOException {
       if (ByteOrder.nativeOrder().equals(ByteOrder.BIG_ENDIAN)) {
            System.out.println("BigEndian");
        } else {
            System.out.println("LittleEndian");
        } 
    }
}
