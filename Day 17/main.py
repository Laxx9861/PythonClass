from view.design import homepage
from controller.contactcontroller import getContact, add, deletecontact
user_choice = homepage()

if user_choice == 1:
    data = getContact()
    for i in data:
        print(f"Name is {i.name} phone is {i.phone}.")
elif user_choice == 2:
    add()  
elif user_choice == 3:
    name = input("Enter name to delete: ")
    if deletecontact(name):
        print("Deleted successfully") 
    else:
        print("Error while delete")       

