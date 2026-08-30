cart = {}


def add_item(name, price):
    global cart
    cart[name] = price


sum=0

for i in range(3):
    item_name = input("Enter item name: ")
    price = int(input("Enter price: "))
    
    sum += price

    add_item(item_name, price)
    


print("Cart:", cart)

unique_items = set(cart)
print("Unique items:", unique_items)

print("Manual sum : ", sum )
