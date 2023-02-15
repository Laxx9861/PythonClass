#Define price and assign value 500, 
# if price is less than or equal to 400 then print price is okay, 
# else print price is high.

price = input("Enter price: ")
price = float(price)
if price<=400:
    print("price is okay")
else: 
    print("price is high")
