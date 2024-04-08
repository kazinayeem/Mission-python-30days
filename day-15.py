# Day 15: Review and practice

# Let's create a program that simulates a simple inventory system using OOP concepts

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print(f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print(f"Quantity of {self.name} updated to {self.quantity}")

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to inventory")

    def display_inventory(self):
        print("Inventory:")
        for product in self.products:
            product.display_product()

# Let's test our inventory system
inventory = Inventory()

# Adding products
product1 = Product("Laptop", 1000, 10)
inventory.add_product(product1)

product2 = Product("Phone", 500, 20)
inventory.add_product(product2)

# Displaying inventory
inventory.display_inventory()

# Updating quantity
product1.update_quantity(8)

# Displaying inventory again
inventory.display_inventory()
