# Voter or Non Voter
# Age > 18 voter else
# use function

def voter_check(a):
    if a>=18:
        print("Voter")
    else:
        print("Non voter") 

age  = int(input("Enter the person age: "))
voter_check(age)

