ph=int(input("Enter ph value "))

if ph>=1 and ph<=3:
    print("Strongly Acidic")
elif ph>=4 and ph<=6:
    print("Weak Acid")
elif ph==7:
    print("Neutral")
elif ph>=8 and ph<=11:
    print("Weak base")
elif ph>=12 and ph<=14:
    print("Strong base")
else:
    print("Not valid ph level")