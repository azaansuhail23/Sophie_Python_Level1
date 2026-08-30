def Check_Prime(n):
    if n==2:
        return True
    
    for i in range(3, n):
        if n % i == 0:
            return False

    return True


res=Check_Prime(31)
print(res)