public class try_and_catch {
    public static void main(String[] args) {
        //tries code
        try {
          int[] myNumbers = {1, 2, 3};
          System.out.println(myNumbers[2]);
        //plays if certein error is found
        } catch (Exception e) {
          System.out.println("Something went wrong.");
        } finally {
            //plays after try/catch regardless of result
            System.out.println("The 'try catch' is finished.");
        }
        checkAge(15);
    }
    static void checkAge(int age) {
        if (age < 18) {
          throw new ArithmeticException("Access denied - You must be at least 18 years old.");
        }
        else {
          System.out.println("Access granted - You are old enough!");
        }
      }
    //all exceptions (one of these exceptions then e) - Ex: catch (ArithmeticException e)
    //Exeption: all exceptions
    //ArithmeticException: It is thrown when an exceptional condition has occurred in an arithmetic operation.
    //ArrayIndexOutOfBoundsException: It is thrown to indicate that an array has been accessed with an illegal index. The index is either negative or greater than or equal to the size of the array.
    //ClassNotFoundException: This Exception is raised when we try to access a class whose definition is not found
    //FileNotFoundException: This Exception is raised when a file is not accessible or does not open.
    //IOException: It is thrown when an input-output operation failed or interrupted
    //InterruptedException: It is thrown when a thread is waiting, sleeping, or doing some processing, and it is interrupted.
    //NoSuchFieldException: It is thrown when a class does not contain the field (or variable) specified
    //NoSuchMethodException: It is thrown when accessing a method that is not found.
    //NullPointerException: This exception is raised when referring to the members of a null object. Null represents nothing
    //NumberFormatException: This exception is raised when a method could not convert a string into a numeric format.
    //RuntimeException: This represents an exception that occurs during runtime.
    //StringIndexOutOfBoundsException: It is thrown by String class methods to indicate that an index is either negative or greater than the size of the string
    //IllegalArgumentException : This exception will throw the error or error statement when the method receives an argument which is not accurately fit to the given relation or condition. It comes under the unchecked exception. 
    //IllegalStateException : This exception will throw an error or error message when the method is not accessed for the particular operation in the application. It comes under the unchecked exception.
}
