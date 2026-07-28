weight = float(input("Enter the weight (kg): "))
height = float(input("Enter the height (cm): "))

height = height / 100

bmi = weight / (height**2)

if bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Healthy")
else:
    print("Underweight")
