# Example of List, Set, Tuple, and Dictonary

#List
# List is a collection which is ordered and changeable. It allows duplicates. []
# Tuple is a collection which is ordered and unchangeable.  It allows duplicates. ()
# Set is a collection which is unordered, unchangeable. It doesn’t allow duplicates. {}
# Dictionary is a collection which is ordered and changeable. No duplicate keys. {}

names = ["Ram", "hari", "Gopal"]
names[1] ="Sarita"
# It is ordered means you can access with index value like names[0]
print(names[0])
print(names[1])


tuplenames =  ("Ram", "hari", "Gopal")


fruits = {"apple", "orange"}


capitalcity = {
    "nepal": "Kathmandu",
    "us": "DC"
}

capitalcity["us"] = "WDC"

print(capitalcity["us"])