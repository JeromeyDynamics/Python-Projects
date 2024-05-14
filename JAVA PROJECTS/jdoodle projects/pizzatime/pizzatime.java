public class pizzatime {
    public static void main(String args[]) {
        String pizza[] = {"plain", "pepperoni", "mushrooms", "sausage"}; //
        String drink[] = {"tub"};
        int wings[] = {20};
        boolean coupon = true; //for 20%
        int t = 13;
        Double total = Double.valueOf(t);
        orderCost(pizza, drink, wings, total);
        double roundedTotal = total/6.625+total;
        if (coupon == true) {
            roundedTotal *= 0.8;
        }
        roundedTotal = (double)Math.round(roundedTotal*100d)/100d;
        System.out.println("Total: $" + roundedTotal);
    }
    public static void orderCost(String[] pizza, String[] drink, int[] wings, Double total) {
        for (String a : pizza) {
            if (a == "pepperoni") {
                total += 1;
            }
            if (a == "mushrooms") {
                total += 0.5;
            }
            if (a == "olives") {
                total += 0.5;
            }
            if (a == "anchovies") {
                total += 2;
            }
            if (a == "sausage") {
                total += 1.5;
            }
        }
        for (String b : drink) {
            if (b == "small") {
                total += 2;
            }
            if (b == "medium") {
                total += 3;
            }
            if (b == "large") {
                total += 3.5;
            }
            if (b == "tub") {
                total += 3.75;
            }
        }
        for (int c : wings) {
            if (c == 10) {
                total += 5;
            }
            if (c == 20) {
                total += 9;
            }
            if (c == 40) {
                total += 17.5;
            }
            if (c == 100) {
                total += 48;
            }
        }
    }
}
//if time=pizzatime
//then Jerome=happy