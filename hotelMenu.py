# Define the menu of the restaurant
menu = {
    'pizza': 100,
    'pasta': 60,
    'burger': 80,
    'coffee': 40,
    'maggy': 30
}

# Greet
print("Welcome to Radhe Restaurant")
print("MENUE CARD : ")
for item, price in menu.items():
    print(f"{item.capitalize()} : {price}")

# Create an Order total Variable (for storing the value like the price of the item)
order_total = 0

# Create a new variable to use for the order from the User
item_1 = input("Enter the name of item you want to order = ").lower()

# Check if the menu item is available in the restaurant
if item_1 in menu:
    order_total += menu[item_1]  # Update the order (0+100 for "Pizza")
    print(f"Your item {item_1.capitalize()} has been added to your order \n")

else:
    print(f"Ordered item {item_1.capitalize()} is not available yet! \n")

# Add another order to the first order
another_order = input("Do you want to add another item? (Yes/No) \n").lower()

if another_order == "yes":
    item_2 = input("Enter the name of the item = \n").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2.capitalize()} has been added to the order")

    else:
        print(f"Item {item_2.capitalize()} is not available!")

print(f"Total amount of items to pay is {order_total}")
