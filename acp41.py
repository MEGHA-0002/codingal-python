# =====================================
# ACTIVITY 70: Length Converter App
# =====================================

from tkinter import *

# Function to convert inches to centimeters
def convert():
    inches = float(entry.get())
    centimeters = inches * 2.54
    result_label.config(
        text=f"{inches} inches = {centimeters:.2f} cm"
    )

# Create window
root = Tk()
root.title("Length Converter")
root.geometry("300x200")

# Heading
Label(root, text="Length Converter",
      font=("Arial", 14)).pack(pady=10)

# Input field
Label(root, text="Enter length in inches:").pack()

entry = Entry(root)
entry.pack(pady=5)

# Convert button
Button(root,
       text="Convert",
       command=convert).pack(pady=10)

# Result label
result_label = Label(root, text="")
result_label.pack()

# Run application
root.mainloop()