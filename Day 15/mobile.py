class Mobile:
    def __init__(self, name , price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Name is: {self.name} ")    
        print(f"Price is: ${self.price} ")    

class Samsung(Mobile):
    def __init__(self, frngerprint):
        self.frngerprint = frngerprint   
        Mobile.__init__(self, "Samsung", 250)

    def display(self):
        super().display()
        print(f"Fingerprint is {self.frngerprint} ")
            



mobile = Mobile ("Samsung", 999)
mobile.display()


mobile2 = Samsung("Enabled")
mobile2.display()