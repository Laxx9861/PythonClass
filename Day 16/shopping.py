class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def __str__(self):
        return f"{self.name} - ${self.price} ({self.stock} in stock)"

class ShoppingCart:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def remove_product(self, product):
        self.products.remove(product)
    
    def total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

# Example usage
shirt = Product("Shirt", 20, 5)
pants = Product("Pants", 30, 3)

cart = ShoppingCart()
cart.add_product(shirt)
cart.add_product(pants)

print("Products in cart:")
for product in cart.products:
    print(product)

print(f"Total: ${cart.total()}")
