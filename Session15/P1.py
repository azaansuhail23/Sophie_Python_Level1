for row in range(10):
    for col in range(5):
        if row==0 or row==9 or col==0 or col==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()