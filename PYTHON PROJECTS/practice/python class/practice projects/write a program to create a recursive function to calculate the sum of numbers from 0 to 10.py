#write a program to create a recursive function(to use the function in the function) to calculate the sum of numbers from 0 to 10

def addition(num):
    if num > 0:
#the addition(num-1) makes it repeat over and over again as long as the if is true while just num-1 repeats once
        answer = num + addition(num-1)
        return answer
    else:
        return 0
#gives addition the value 10
print(addition(10))
# 10 9 8 7 6 5 4 3 2 1
print("----------------------------------------------------")

#write a program to create a function that takes two keyword arguments, name and age, and print there value

def person(name, age):
    return name,age

print(person(name = "Mr. Butterscotch", age = 45))