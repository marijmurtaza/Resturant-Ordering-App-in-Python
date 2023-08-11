import datetime

class MenuItem:
    def __init__(self, name, price, preparation_time):
        self.name = name
        self.price = price
        self.preparation_time = preparation_time

class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

class Order:
    def __init__(self):
        self.items = []
        self.total = 0
        self.discount = 0
        self.preparation_time = 0

    def add_item(self, item, quantity):
        order_item = OrderItem(item, quantity)
        self.items.append(order_item)
        self.total += item.price * quantity
        self.preparation_time += item.preparation_time * quantity

    def apply_discount(self):
        sandwich_count = 0
        salad_count = 0
        soup_count = 0

        for item in self.items:
            item_name = item.menu_item.name
            if item_name == 'sandwich':
                sandwich_count += item.quantity
            elif item_name == 'salad':
                salad_count += item.quantity
            elif item_name == 'soup':
                soup_count += item.quantity

        if sandwich_count >= 5:
            self.discount += self.total * 0.1
        if salad_count > 0 and soup_count > 0:
            self.discount += self.total * 0.1
        if soup_count > 0 and (sandwich_count > 0 or salad_count > 0):
            self.discount += self.total * 0.2

    def calculate_total(self):
        self.total -= self.discount

    def print_receipt(self, name):
        print("*************************************************")
        print(f"{name}, thanks for your order")
        print("Items\t\tQty\tPrice")
        for item in self.items:
            total_price = item.menu_item.price * item.quantity
            print(f"{item.menu_item.name}\t{item.quantity}\t${total_price}")
        tax = self.total * 0.1
        total_with_tax = self.total + tax
        print(f"Tax\t\t\t\t${tax:.2f}")
        print(f"Total\t\t\t\t${total_with_tax:.2f}")
        print(f"{datetime.date.today()}, Your order will be ready in {self.preparation_time} mins")
        print("*************************************************")


# Menu items
sandwich = MenuItem('sandwich', 10, 5)
salad = MenuItem('salad', 8, 8)
soup = MenuItem('soup', 6, 15)
tea_coffee = MenuItem('tea/coffee', 5, 5)

# Create an order
order = Order()

# Take user input for selecting items and quantities
name = input("Please enter your name: ")

while True:
    print("\nMenu:")
    print("1. Sandwich")
    print("2. Salad")
    print("3. Soup")
    print("4. Tea/Coffee")
    print("5. Checkout and Print Receipt")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        quantity = int(input("Enter the quantity: "))
        order.add_item(sandwich, quantity)
        print(f"{quantity} sandwich(es) added to your order.")
    elif choice == '2':
        quantity = int(input("Enter the quantity: "))
        order.add_item(salad, quantity)
        print(f"{quantity} salad(s) added to your order.")
    elif choice == '3':
        quantity = int(input("Enter the quantity: "))
        order.add_item(soup, quantity)
        print(f"{quantity} soup(s) added to your order.")
    elif choice == '4':
        quantity = int(input("Enter the quantity: "))
        order.add_item(tea_coffee, quantity)
        print(f"{quantity} tea/coffee added to your order.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

# Apply discounts and calculate total
order.apply_discount()
order.calculate_total()

# Print the receipt
order.print_receipt(name)
