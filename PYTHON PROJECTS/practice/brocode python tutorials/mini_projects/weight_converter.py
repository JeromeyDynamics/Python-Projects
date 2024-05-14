weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (Kgs or Lbs): ") #the opposite of the one u chose

if unit == "Lbs":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "Kgs":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")