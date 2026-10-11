# Restaurant Order System

menu = {
    "Pizza": 500,
    "Burger": 250,
    "Pasta": 350,
    "Momo": 200,
    "Sandwich": 180,
    "Fries": 150,
    "Coffee": 120,
    "Tea": 80
}

order = []

def display_menu():
    print("\nMenu")
    for item, price in menu.items():
        print(item, "-", price)

def add_order(item, qty):
    order.append((item, qty))

def calculate_bill():
    subtotal = 0

    for item, qty in order:
        subtotal += menu[item] * qty

    tax = subtotal * 0.10
    total = subtotal + tax

    return subtotal, tax, total

display_menu()

while True:
    try:
        item = input("Enter food item: ")

        if item not in menu:
            raise KeyError

        qty = int(input("Enter quantity: "))

        if qty <= 0:
            raise ValueError

        add_order(item, qty)

        more = input("Order more? (yes/no): ")

        if more.lower() != "yes":
            break

    except KeyError:
        print("Food item does not exist.")

    except ValueError:
        print("Invalid quantity.")

print("\nFinal Order")
for item, qty in order:
    print(item, "-", qty)

subtotal, tax, total = calculate_bill()

print("Subtotal =", subtotal)
print("Tax =", tax)
print("Final Bill=", total)
