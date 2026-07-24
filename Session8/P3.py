number = int(input("Enter the number "))


if number > 0:
    if number % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    if number % 2 == 0:
        print("Negative Even Number")
    else:
        print("Negative Odd Number")
