print("------------------------")
print("Laxman Contact Book")
print("1. List Contact")
print("2. Add Contact")

choice = int(input("Enter your choice [1/2]: "))

if choice == 1:
    f = open("ok.csv", "r")
    print(f.read())
    f.close()

if choice == 2:
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    f = open("ok.csv", "a")
    f.write(f"\n{name},{phone}")
    f.close()
    print("Contact saved successfully.")