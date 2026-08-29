def factorial(n):
    fact=1
    i=1
    
    while(i<=n):
        fact=fact*i
        
        i=i+1
    
    return fact

res=factorial(5)
print(res)

#variable
def average(*numbers):
    sum =0
    
    for i in numbers:
        sum =sum +i
        
    return sum/len(numbers)


avg=average(6,7,6,9,10)
print("Average=",avg)