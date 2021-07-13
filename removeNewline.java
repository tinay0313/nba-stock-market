import java.io.*;
import java.util.regex.Pattern;

public class removeNewline {
    private static void printRow(String[] data, PrintStream output) {
        output.printf("%s,%s,%s\n", data[0], data[1], data[2]);
    }

    public static void main(String[] args) throws IOException {
        String dateregex = "^20[0-9][0-9]-[0-9][0-9]-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9]+.*";
        BufferedReader reader = new BufferedReader(new FileReader("twitterScrapeOutput1011.csv"));
        FileOutputStream fout = new FileOutputStream("twitterScrapeOutput1011_nonew.csv");
        PrintStream output = new PrintStream(fout);

        String row = reader.readLine();
        output.println(row);
        row = reader.readLine();

        while( row != null ) {
            String[] data = row.split(",",3);
            String text = data[2];
            String next = "";
            if(!(text.matches(".*,[0-9]*.[0-9]$"))) {
                next = reader.readLine();
                while(next != null && !next.matches(dateregex)) {
                    if(next.matches(".*,[0-9]*.[0-9]$")) {
                        String[] temp = next.split(",");
                        int i = 0;
                        for(; i < temp.length - 6; i++) {
                            data[2] += temp[i];
                        }
                        for(; i < temp.length - 1; i++) {
                            data[2] += temp[i] + ",";
                        }
                        data[2] += temp[i];
                    } else {
                        data[2] += " " + next;
                    }
                    next = reader.readLine();
                }
            }
            printRow(data, output);

            if(next != null && next.matches(dateregex)) {
                row = next;
            } else {
                row = reader.readLine();
            }
        }
        reader.close();
    }
}