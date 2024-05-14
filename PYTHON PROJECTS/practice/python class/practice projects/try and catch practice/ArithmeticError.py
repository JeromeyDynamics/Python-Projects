def division_calculator(num1, num2):
    try:
        result = num1/num2
        print("Result: ", result)
    except ArithmeticError: 
        print("Arithmetic error, try again")
    else:
        result = result*100
        print("Grade: ", str(round(result)) + "%")
    finally:
        print(":)")
        
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the first number: "))
division_calculator(num1, num2)