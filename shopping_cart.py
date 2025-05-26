#Student name: Andrea Phan
#Date: May 25, 2025

#This This program simulates a simple shopping cart.
#Users can add items, specify quantities, and see the total cost.
#The program uses exception handling to manage invalid inputs.

print("Welcome to the Shopping Cart Program!")

while True:
    total_cost = 0
    item_number = int(input("How many items do you want to buy?"))

    while item_number > 0:
        try:
            name = input("What item do you want to buy?")
            item_price = float(input("How much does an item cost in dollars?"))
            item_quantity = int(input("What is the quantity?"))
            item_cost = item_price * item_quantity
            total_cost += item_cost 
            item_number -= 1
        except:
            print("Error: Your input is invalid. Please retype the item information.")
            continue

    if total_cost > 100:
        discount = total_cost * 0.1
        total_cost -= discount
        print(f"\nYou saved ${discount:.2f} with a 10% discount!")
        print(f"Discount Total: ${total_cost}")
    else: 
        print("Your total cost is ", total_cost)

    restart = input("Would you like to restart the program? (Yes/No):")
    if restart == 'No':
        print("\nThank you for shopping with us!")
        break


