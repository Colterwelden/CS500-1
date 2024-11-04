class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found.")

    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}")


def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )
    choice = ""
    while choice != "q":
        print(menu)
        choice = input("Choose an option: ").strip().lower()
        if choice == "a":
            item_name = input("Enter the item name: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            new_item = ItemToPurchase(item_name, item_price, item_quantity)
            cart.add_item(new_item)
        elif choice == "r":
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)
        elif choice == "c":
            item_name = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            modified_item = ItemToPurchase(item_name, item_quantity=new_quantity)  # corrected line
            cart.modify_item(modified_item)
        elif choice == "i":
            cart.print_descriptions()
        elif choice == "o":
            cart.print_total()
        elif choice == "q":
            print("Exiting the menu.")
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)
