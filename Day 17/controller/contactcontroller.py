

def getContact():
    f = open("ok.csv", "r")
    contactlist = []
    for i in f:
        i = i.replace("\n", "")
        valueinlist = i.split(",")
        if(valueinlist[0] != "name"):
            c = Contact(valueinlist[0], valueinlist[1])
            contactlist.append(c)
    return contactlist

def add():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    f = open("ok.csv", "a")
    f.write(f"\n{name},{phone}")
    f.close()
    print("Contact saved successfully.")

def savetoscv(listcontact):
    csv = "name,phone\n"
    for contact in listcontact:
        csv += f"{contact.name},{contact.phone}\n"
    csv = csv.strip()
    f = open("ok.csv", "w")
    f.write(csv)
    f.close()

def deletecontact(name):
    deleted = False
    allcontact = getContact()
    for i in allcontact:
        if i.name == name:
            allcontact.remove(i)
            deleted =True
    savetoscv(allcontact)
    return deleted


    
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        print(f"Name is {self.name}, phone is {self.phone}")        