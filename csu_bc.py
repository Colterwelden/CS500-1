print("Welcome to the CSU Global Bookstore Rewards Club!")
books_purchased = int(input("Enter the number of books purchased this month: "))


if books_purchased == 0:
    points_awarded = 0
elif books_purchased == 2:
    points_awarded = 5
elif books_purchased == 4:
    points_awarded = 15
elif books_purchased == 6:
    points_awarded = 30
elif books_purchased >= 8:
    points_awarded = 60
else:
    points_awarded = 0

print(f"The purchase of {books_purchased} books has earned you {points_awarded} points.")
input("Press Enter to close...")
