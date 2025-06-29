# Create a shopping chart programme that will continuously ask the user for a food product and the price of the product.
# Have an exit clause if the user wishes to stop adding more things to their charts.
# At the end of the show the food items and the total cost to the user.

# Lists to store items and their prices
foods = []
prices = []

# Variable to hold total cost
total = 0

while True:
    # Ask the user for the food item
    food = input("Enter a food to buy or press 'q' to quit: ")

    # Exit condition
    if food.lower() == 'q':
        break

    # Ask for the price of the food
    try:
        price = float(input(f"Enter the price of {food}: R"))
        foods.append(food)
        prices.append(price)
    except ValueError:
        print("❌ Invalid input! Please enter a valid number for the price.\n")

# Display the final shopping cart
print("\n----- 🧾 YOUR CART -----")
for i in range(len(foods)):
    print(f"{foods[i]} - R{prices[i]:.2f}")
    total += prices[i]

# Show total cost
print("\n💰 Total Cost: R{:.2f}".format(total))
    