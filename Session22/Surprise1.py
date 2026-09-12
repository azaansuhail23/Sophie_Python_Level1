# Take three no. from the user and you have to find the maximum no. among all of them.

a=int(input("Enter the first no. "))
b=int(input("Enter the second no. "))
c=int(input("Enter the third no. "))


if a>b and a>c:
    print("a is largest no. ")
elif b>a and b>c:
    print("b is largest no. ")
else:
    print("c is largest no. ")
    
    
#Method

largest=max(a,max(b,c))
print(largest)