import tkinter as tk
window = tk.Tk()
window.geometry("700x500")


label = tk.Label(
    text="Laxman Phonebook",
    foreground="white",  # Set the text color to white
    background="black", # Set the background color to black
)


def save():
    name = nameentry.get()
    phone = phoneentry.get()
    f = open("laxmans.txt", "w")
    f.write(f"{name}, {phone}")
    print("Write successful")
    f.close()

label.pack()

labelname = tk.Label(text="Enter name: ",)
labelname.pack()
nameentry = tk.Entry(fg="yellow", bg="gray", width=50, )
nameentry.pack()
labelphone = tk.Label(text="Enter phone: ",)
labelphone.pack()
phoneentry = tk.Entry(fg="yellow", bg="gray", width=50)
phoneentry.pack()
savebutton = tk.Button(
    text="Save",
    bg="gray",
    fg="yellow",
    command=save
)

savebutton.pack()


window.mainloop()