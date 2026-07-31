balance = []

operation = int(
    input(
        "Press 1 to check the balance\n Press2 to withdraw amount\n Press 3 to add amount\n Enter : "
    )
)

if operation == 1:
    if sum(balance) > 0:
        print(sum(balance))
    else:
        print("No balance")
        
elif operation == 2:
    if sum(balance) > 0:
        print(sum(balance))
        print(balance.pop())
    else:
        print("Insufficient balance")
elif operation==3:
    amount=int(input("Enter the amount "))
    
    balance.append(amount)
    print(sum(balance))
else:
    print("Invalid Bank Operation")