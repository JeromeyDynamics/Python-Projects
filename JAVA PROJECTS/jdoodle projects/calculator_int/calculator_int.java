import java.util.Scanner;

public class calculator_int {
    public static void main(String[] args) {
        System.out.println("Calculator type (*,/,+,-):");
        Scanner sc = new Scanner(System.in);
        String type = sc.nextLine();
        if (type.equals("*")) {
            double mult1 = sc.nextInt();
            double mult2 = sc.nextInt();
            System.out.print(mult1 * mult2);
        } else if (type.equals("/")) {
            double div1 = sc.nextInt();
            double div2 = sc.nextInt();
            System.out.println(div1 / div2);
        } else if (type.equals("+")) {
            double add1 = sc.nextInt();
            double add2 = sc.nextInt();
            System.out.println(add1 + add2);
        } else if (type.equals("-")) {
            double sub1 = sc.nextInt();
            double sub2 = sc.nextInt();
            System.out.println(sub1 - sub2);
        } else {
            System.out.println("Error try again :(");
        }
        sc.close();
    }
}
