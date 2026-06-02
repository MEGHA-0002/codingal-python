# =====================================
# ACTIVITY 74: Password Strength Checker App
# =====================================

from tkinter import *

# Function to check password strength
def check_strength():

    password = entry.get()
    length = len(password)

    if length < 6:
        result.config(text="Password Strength: Weak")
    elif length < 10:
        result.config(text="Password Strength: Medium")
    else:
        result.config(text="Password Strength: Strong")

# Create main window
root = Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

# Heading
Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 14)
).pack(pady=10)

# Password input
Label(root, text="Enter Password:").pack()

entry = Entry(root, show="*")
entry.pack(pady=5)

# Check button
Button(
    root,
    text="Check Strength",
    command=check_strength
).pack(pady=10)

# Result label
result = Label(root, text="")
result.pack()

# Run application
root.mainloop()