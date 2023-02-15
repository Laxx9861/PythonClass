# 10%
# $0 to $10,275.
# 12%
# $10,276 to $41,775.
# 22%
# $41,776 to $89,075.
# 24%
# $89,076 to $170,050.
# 32%
# $170,051 to $215,950.
# 35%

# $215,951 to $539,900.
# 37%
# $539,901 or more.

income = float(input("Enter total income: "))

if income >=0 and income <=10275:
    print("You need to pay 10% tax.")
    tax = 10/100 * income
    print(f"Total tax is {tax}.")
elif income >= 10276 and income <= 41775:
    print("You need to pay 12% tax.") 
    tax = 12/100 * income
    print(f"Total tax is {tax}.")
elif income >=41776 and income <=89075:
    print("You need to pay 22% tax.")
    tax = 22/100 * income
    print(f"Total tax is {tax}.")
elif income >=89076 and income <=170050:
    print("You need to pay 24% tax.")
    tax = 24/100 * income
    print(f"Total tax is {tax}")
elif income >=170051 and income<=215950:
    print("You need to pay 32% tax.")
    tax = 32/100 * income
    print(f"Total tax is {tax}")
elif income >=215951 and income<=539900:
    print("You need to pay 35% tax.")
    tax = 35/100 * income
    print(f"Total tax is {tax}")
elif income >=539901:
    print("You need to pay 37% tax. ")
    tax = 37/100 * income
    print(f"Total tax is {tax}")
else:
    print("Invalid income")    


