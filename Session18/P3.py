# Call by value Vs Call by reference

def f1():
    x=20
    
    print("Inside function : ", x) 

x=14

f1()

print("Outside the function : ",x)

print("--------------")

#call by reference : Changes reflects 
def f2(numbers):
    numbers.append(24)
    
    print("Inside function : ",numbers)
    

numbers=[10,20,30,66]

f2(numbers)

print("Outside function : ",numbers)