s1=input("Enter the first string")
s2=input("Enter the second string")
s3=input("Enter the third string")
s4=input("Enter the fourth string")
s5=input("Enter the fifth string")


list=[]
list.append(s1)
list.append(s2)
list.append(s3)
list.append(s4)
list.append(s5)

print(type(list))

tp=tuple(list)
print(tp)
print(type(tp))