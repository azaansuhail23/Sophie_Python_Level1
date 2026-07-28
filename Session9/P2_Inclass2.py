year=int(input("Enter the year "))

#? leap year ==> 365+1=366 days 
#* 2028 2032

if ((year%4==0) and (year%100!=0 or year%400==0)):
    print("Leap Year")
else:
    print("Normal Year")