import tkinter as tk

def add_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    result_label.config(text="Result: {}".format(result))

root = tk.Tk()
root.title("Add Numbers")

label1 = tk.Label(root, text="Number 1")
label2 = tk.Label(root, text="Number 2")
result_label = tk.Label(root, text="")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

add_button = tk.Button(root, text="Add", command=add_numbers)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
result_label.grid(row=2, column=1)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

add_button.grid(row=2, column=0)

root.mainloop()
