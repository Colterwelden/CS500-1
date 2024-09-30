# Critical Thinking Module 3

# Get input from the user and convert to float
cost_of_meal = float(input("Enter the cost of your meal: "))

# Calculate tip and sales tax
tip = cost_of_meal * 0.18
sales_tax = cost_of_meal * 0.07
total = cost_of_meal + tip + sales_tax

# Print the total cost using an f-string
print(f"The cost of your meal including a tip and sales tax is: ${total:f}")
input("Press Enter to close...")