# Here birthyear is parameter
def age_finder(birthyear):
    age = 2023 - birthyear
    print(f"Your age is {age}")

def add(num1, num2):
    sum = num1 + num2
    print(f"The sum is {sum}")



age_finder(1997)
age_finder(1998)
age_finder(1999)
age_finder(2000)
age_finder(2001)

add(20,50)


# Write function to calculate simple interest
# Formula: p* t * r / 100

# Write a program to find simple interst. Formula [p*t*r/100]
principal = 2000
time = 2
rate = 10

si= principal*time*rate/100
print("simple interest is ",si)