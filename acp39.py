
# Import tkinter library
from tkinter import *

# Create window
root = Tk()
root.title("Product Calculator")
root.geometry("300x250")

# Function to calculate product
def calculate_product():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    product = num1 * num2
    result_label.config(text="Product = " + str(product))

# Labels
label1 = Label(root, text="Enter First Number:")
label1.pack()

# Entry for first number
entry1 = Entry(root)
entry1.pack()

# Label for second number
label2 = Label(root, text="Enter Second Number:")
label2.pack()

# Entry for second number
entry2 = Entry(root)
entry2.pack()

# Button to calculate product
button = Button(root, text="Find Product",
                command=calculate_product)
button.pack(pady=10)

# Label to display result
result_label = Label(root, text="")
result_label.pack()

# Run application
root.mainloop()