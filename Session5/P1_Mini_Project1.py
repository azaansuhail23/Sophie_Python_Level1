# 	1. Name --> input()
# 	2. 3subjects_marks--> input()
# 	3. Sum
# 	4. Appying the criteria
# 	5. Finding the average
#   Printing the result using f string.

name=input("Enter your name please ")

subject1=int(input("Enter the marks "))
subject2=int(input("Enter the marks "))
subject3=int(input("Enter the marks "))

total_sum=subject1+subject2+subject3

#Conditional Statement
if total_sum > 150:
    print("Passed")
else:
    print("Failed")

average_marks=total_sum//3

print(f"{name} is getting {total_sum} marks out of 300 and the average marks is {average_marks}")

