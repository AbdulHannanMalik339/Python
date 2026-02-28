height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print("Your BMI is: ", bmi)

if bmi < 18.4:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 24.9:
    print("You are normal weight.")
elif bmi >= 25 and bmi < 29.9:
    print("You are overweight.")
else: 
    if bmi >= 30 and bmi < 34.9:
        print("You are obese.")
    else:
        print("You are extremely obese.")