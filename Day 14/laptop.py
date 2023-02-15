
# Create Laptop Class[name, price] and Create 3 Laptop Object and Print All Details
class laptop:
    def __init__(self, name, price):
        self.name =name
        self.price = price
        

    def display(self):
        print(f"Laptop name is {self.name}")       
        print(f"Price is {self.price}")      

    def __str__(self):
        return self.name  

f1 = laptop("Apple", 2000,)
f1.display()
