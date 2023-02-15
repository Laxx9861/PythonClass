class Freeze:
    def __init__(self, name, brand, price, waranty):
        self.name =name
        self.brand= brand
        self.price = price
        self.waranty = waranty

    def display(self):
        print(f"Freeze name is {self.name}")    
        print(f"Brand name is {self.brand}")    
        print(f"Price is {self.price}")    
        print(f"Warranty is {self.waranty}")  

    def __str__(self):
        return self.name    


f1 = Freeze("LG Freeze", "LG", 350, 2)
f1.display()


f2 = Freeze("CG", "CG", 360, 3)
f2.display()
print(f2)

# Create Laptop Class[name, price] and Create 3 Laptop Object and Print All Details