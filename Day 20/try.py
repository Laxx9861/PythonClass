## 
try: 
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = num1 + num2
    print(sum)
except:
    print("You can enter only numbers")

finally:
    print("Hello")   
