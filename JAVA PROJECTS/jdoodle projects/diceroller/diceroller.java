public class diceroller {
    public static void main(String[] args) {
        // java always rounds down so + 1
        int dice1 = (int) (Math.random() * 6 + 1);
        int dice2 = (int) (Math.random() * 6 + 1);
        System.out.println("dice 1: " + dice1);
        System.out.println("dice 2: " + dice2);
        System.out.println("dice total: " + (dice1 + dice2));
    }
}
