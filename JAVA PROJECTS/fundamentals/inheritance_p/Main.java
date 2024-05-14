//find in the future why it only works with debug and run

package inheritance_p;

public class Main {

    public static void main(String[] args) {

        // inheritance = the process where one class acquires,

        // the attributes and methods of another.

        Car car = new Car();

        car.go();

        Bicycle bike = new Bicycle();

        car.go();
        bike.stop();

        System.out.println(car.doors);
        System.out.println(bike.pedals);
    }
}