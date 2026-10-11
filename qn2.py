# Shopping Cart

products = {
    "Laptop": {"price": 50000, "quantity": 5},
    "Mouse": {"price": 500, "quantity": 10},
    "Keyboard": {"price": 1500, "quantity": 8},
    "Monitor": {"price": 20000, "quantity": 4},
    "Speaker": {"price": 3000, "quantity": 6},
    "Headphone": {"price": 2500, "quantity": 7}
}

cart = {}

def add_to_cart(product, qty):
    cart[product] = cart.get(product, 0) + qty

def calculate_total():
    total = 0
    for item, qty in cart.items():
        total += products[item]["price"] * qty
    return total

def display_cart():
    print("\nCart Items:")
    for item, qty in cart.items():
        print(item, "-", qty)

while True:
    try:
        product = input("Enter product name: ")

        if product not in products:
            raise KeyError

        qty = int(input("Enter quantity: "))

        if qty > products[product]["quantity"]:
            print("Requested quantity exceeds available stock.")
        else:
            add_to_cart(product, qty)

        choice = input("Add more items? (yes/no): ")
        if choice.lower() != "yes":
            break

    except KeyError:
        print("Product does not exist.")

    except ValueError:
        print("Invalid quantity.")

display_cart()
print("Final Bill =", calculate_total())

