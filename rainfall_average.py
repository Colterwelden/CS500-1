
num_years = int(input("Enter the number of years: "))


rainfall_total = 0
months_total = 0 

for year in range(1, num_years + 1):
    print(f"\nYear {year}:")
    
 
    for month in range(1, 13):
        # Get the rainfall for the current month and convert to float
        rainfall = float(input(f"Enter the amount of rainfall in inches for month {month}: "))
        # Add the rainfall to the total
        rainfall_total += rainfall
        # Increment the total number of months
        months_total += 1


rainfall_average = rainfall_total / months_total


print(f"\nTotal number of months: {months_total}")
print(f"Total inches of rainfall: {rainfall_total:.2f}")
print(f"Average rainfall per month: {rainfall_average:.2f} inches")

input("Press Enter to close...")
