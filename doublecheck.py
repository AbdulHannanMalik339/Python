num = int(input("Enter a number: "))

if num > 50:
    print("Number is greater than 50")
    if num%2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is less than 50")