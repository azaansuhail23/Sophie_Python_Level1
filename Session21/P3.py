#First way  --> Loop 
for num in range(1,11):
    print(num)
    
print("-------")

def Print_1_to_10(num):
    #*Base condition
    if(num==11):
        return 
    
    print(num)
    
    #?Recusive Function
    Print_1_to_10(num+1)

Print_1_to_10(1)