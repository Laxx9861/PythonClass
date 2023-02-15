from tkinter import *

root = Tk()
root.geometry("400x400")

Label(root, text="Enter Your Income:").grid(row=0, column=0)
# define the label, step 1
label3 = Label(root)
# set grid, step 2
label3.grid(row=3, column=1)

first_no = IntVar()

# same goes for here
income = Entry(root, textvariable=first_no).grid(row=0, column=1)

def calculate():
    income = first_no.get()
    if income >=0 and income <=10275:
        tax = 10/100 * income
        label3.config(text=f"You need to pay 10% tax. Total tax is {tax}. ")
    elif income >= 10276 and income <= 41775:
        tax = 12/100 * income
        label3.config(text=f"You need to pay 12% tax. Total tax is {tax}. ")
    elif income >=41776 and income <=89075:
        tax = 22/100 * income
        label3.config(text=f"You need to pay 22% tax. Total tax is {tax}. ")
    elif income >=89076 and income <=170050:
        tax = 24/100 * income
        label3.config(text=f"You need to pay 24% tax. Total tax is {tax}. ")
    elif income >=170051 and income<=215950:
        tax = 32/100 * income
        label3.config(text=f"You need to pay 32% tax. Total tax is {tax}. ")
    elif income >=215951 and income<=539900:
        tax = 35/100 * income
        label3.config(text=f"You need to pay 35% tax. Total tax is {tax}. ")
    elif income >=539901:
        tax = 37/100 * income
        label3.config(text=f"You need to pay 37% tax. Total tax is {tax}. ")
    else:
        label3.config(text=f"Invalid income")    

# and here
mybutton = Button(root, text=("Calculate Tax!"), command=calculate).grid(row=2, column=1)

root.mainloop()