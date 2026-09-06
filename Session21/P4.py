def sum_of_natural_number(i,N):
    sum=0
    
    if i==N:
       return sum
   
    sum +=i
    
    sum_of_natural_number(i+1,N)

res=sum_of_natural_number(1,5)
print(res)