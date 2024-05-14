def division_calc(num1, num2):
    print("result: ")
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("undefined")
    #plays if the exception doesn't happen
    else:
        if num1 < num2:
            print("decimals :'(")
    #plays after all
    finally:
        print(":)")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

division_calc(int(num1), int(num2))