my_dict = {
   "apple": 5,
   "mango": 7,
   "banana": 12
}

new_price = {item: value*132.26 for (item, value) in my_dict.items()}

print(new_price)


