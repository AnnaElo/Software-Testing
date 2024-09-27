# Given code from the assignment document
class CartItem :
    def __init__ ( self , name , price , quantity ):
        self . name = name
        self . price = price
        self . quantity = quantity

    def update_quantity ( self , new_quantity ):
        self . quantity = new_quantity

    def get_subtotal ( self ):
        return self . price * self . quantity

# Given code from the assignment document
class Cart :
    def __init__ ( self ) :
        self . items = []

    def add_item ( self , name , price , quantity ):
# Check if item is already in the cart
        for item in self . items :
            if item . name == name :
                item . update_quantity ( item . quantity + quantity )
            return f" Updated { name } quantity to { item . quantity }"
# Add new item to the cart
        new_item = CartItem ( name , price , quantity )
        self . items . append ( new_item )
        return f" Added { name } to cart "

    def remove_item ( self , name ):
        self . items = [ item for item in self . items if item . name != name ]
        return f" Removed { name } from cart "

    def update_item_quantity ( self , name , new_quantity ):
        for item in self . items :
            if item . name == name :
                item . update_quantity ( new_quantity )
                return f" Updated { name } quantity to { new_quantity }"
        return f"{ name } not found in cart "

    def calculate_total ( self ):
        subtotal = sum( item . get_subtotal () for item in self . items )
        tax = subtotal * 0.10 # Assume 10% tax
        delivery_fee = 5.00 # Flat delivery fee
        total = subtotal + tax + delivery_fee
        return {" subtotal ": subtotal , " tax ": tax , " delivery_fee ": delivery_fee , " total ": total }
    
    def view_cart(self):
        return [{"name": item.name, "quantity": item.quantity, "subtotal": item.get_subtotal()} for item in self.items]

# Simple GUI for user, so testing can be run in cmd environment 
def main():
    cart = Cart()
    while True:
        print("\nOptions:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. Update item quantity")
        print("4. View cart")
        print("5. Calculate total")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            print(cart.add_item(name, price, quantity))

        elif choice == "2":
            name = input("Enter item name to remove: ")
            print(cart.remove_item(name))

        elif choice == "3":
            name = input("Enter item name to update: ")
            quantity = int(input("Enter new quantity: "))
            print(cart.update_item_quantity(name, quantity))

        elif choice == "4":
            items = cart.view_cart()
            if not items:
                print("Cart is empty.")
            else:
                for item in items:
                    print(f"Item: {item['name']}, Quantity: {item['quantity']}, Subtotal: {item['subtotal']}")

        elif choice == "5":
            total = cart.calculate_total()
            print(f"Subtotal: {total['subtotal']}")
            print(f"Tax: {total['tax']}")
            print(f"Delivery Fee: {total['delivery_fee']}")
            print(f"Total: {total['total']}")

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid option, please try again.")

# Run the program for testing
if __name__ == "__main__":
    main()