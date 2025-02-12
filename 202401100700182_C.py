# Grocery store calculator using a while loop
total_cost = 0.0

print("Welcome to Siddhant's Grocery Store!")

while True:
    item_name = input("Enter the item name (or type 'done' to finish): ")
    
    if item_name.lower() == 'done':
        break
    
    item_price = float(input(f"Enter the price of {item_name}: "))
    item_quantity = int(input(f"Enter the quantity of {item_name}: "))
    
    total_cost += item_price * item_quantity
    print(f"Added {item_quantity} of {item_name} to your cart. Total cost so far: ${total_cost:.2f}")

print(f"\nYour total cost is: ${total_cost:.2f}")
print("Thank you for shopping with us!")
# Grocery store calculator using a while loop
total_cost = 0.0

print("Welcome to Siddhant's Grocery Store!")

while True:
    item_name = input("Enter the item name (or type 'done' to finish): ")
    
    if item_name.lower() == 'done':
        break
    
    item_price = float(input(f"Enter the price of {item_name}: "))
    item_quantity = int(input(f"Enter the quantity of {item_name}: "))
    
    total_cost += item_price * item_quantity
    print(f"Added {item_quantity} of {item_name} to your cart. Total cost so far: ${total_cost:.2f}")

print(f"\nYour total cost is: ${total_cost:.2f}")
print("Thank you for shopping with us!")
