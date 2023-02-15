# Does the company have a product/service which is earning profit for many years [10-20 yrs]? Futuristic 
# Does management aim to increase sales? 
# Does research and development cost effective from company size?
# Does the company have one or more sales organizations? Is it good marketing?
# Does the company's profit margin is good? Look at the expenses of the company. 
# What company is doing to maintain and improve its profit margin?
# Does the company have a good relationship with workers?
# Does the company have a good relationship with executives?
# Does the company hold management? Does it have multiple managers
# Does the company have good accounting control and cost analysis?

point = 0
answer1 = input("Does the company have a product/service which is earning profit from many years [10-20 yrs]?.")
if answer1 == "yes":
    point = point+1

answer2 = input("Does management aim to increase sales?")
if answer2 == "yes":
    point = point+1

answer3 = input("Does research and development cost effective from company size?")
if answer3 == "yes":
    point = point+1

answer4 = input("Does the company have one or more sales organizations? Is it good marketing?")
if answer4 == "yes":
    point = point+1

answer5 = input("Does the company's profit margin is good? Look at the expenses of the company.")
if answer5 == "yes":
    point = point+1

answer6 = input("What company is doing to maintain and improve its profit margin?")
if answer6 == "yes":
    point = point+1

answer7 = input("Does the company have a good relationship with workers?")
if answer7 == "yes":
    point = point+1

answer8 = input("Does the company have a good relationship with executives?")
if answer8 == "yes":
    point = point+1

answer9 = input("Does the company hold management? Does it have multiple managers")
if answer9 == "yes":
    point = point+1

answer10 = input("Does the company have good accounting control and cost analysis?")
if answer10 == "yes":
    point = point+1


print(f"Total point is {point}")
## Final check
if point>7:
    print("you can invest")
else:
    print("Invest on your risk.")  


