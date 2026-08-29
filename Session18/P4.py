def product(*numbers):
    product=1
    
    for i in numbers:
        product=product * i
    
    return product

numbers=(1,2,3,4,5,67,9,10,6,34)

ans=product(*numbers)
print(ans)