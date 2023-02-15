# Does the company have a product/service which is earning profit from many years.
# Does management aims to increase sales. 
# Does research and development cost is effective from company size.

# If point is more than 2 you can invest
# else print Invest on your risk.

point = 0
answer1 = input("Does the company have a product/service which is earning profit from many years.")
if answer1 == "yes":
    point = point+1

answer2 = input("Does management aims to increase sales? ")
if answer2 == "yes":
    point = point+1

answer3 = input("Does research and development cost is effective from company size? ")
if answer3 == "yes":
    point = point+1


print(f"Total point is {point}")
## Final check
if point>2:
    print("you can invest")
else:
    print("Invest on your risk.")    