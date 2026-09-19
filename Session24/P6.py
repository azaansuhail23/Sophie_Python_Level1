try:
    a=int(input("Enter the first no. "))
    b=int(input("Enter the second no. "))
    
    print(a/b)

except ZeroDivisionError:
    print("Handling zero division error!")
except TypeError:
    print("Handling Type error!")
except ValueError:
    print("Handling value error!")
else:
    print("I am in else block ")
    