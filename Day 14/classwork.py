class WhiteBoard:
    def __init__(self, length, width, price):
        self.length = length
        self.width = width
        self.price = price


# Lets create object from class

w1 = WhiteBoard(25, 30, 3500)
w2 = WhiteBoard(30, 40, 4500)


print(w1.length)
print(w1.price)
print(w2.price)