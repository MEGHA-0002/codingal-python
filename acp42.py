# =====================================
# ACTIVITY 71: Interest Calculator App
# =====================================

from tkinter import *

# Function to calculate Simple Interest and Compound Interest
def calculate_interest():

    P = float(principal_entry.get())
    R = float(rate_entry.get())
    T = float(time_entry.get())

    # Simple Interest
    SI = (P * R * T) / 100

    # Compound Interest
    Amount = P * ((1 + R / 100) ** T)
    CI = Amount - P

    result_label.config(
        text=f"Simple Interest = {SI:.2f}\nCompound Interest = {CI:.2f}"
    )

# Create window
root = Tk()
root.title("Interest Calculator")
root.geometry("350x300")

# Heading
Label(root,
      text="Interest Calculator",
      font=("Arial", 14)).pack(pady=10)

# Principal Amount
Label(root, text="Principal Amount:").pack()
principal_entry = Entry(root)
principal_entry.pack()

# Rate of Interest
Label(root, text="Rate of Interest (%):").pack()
rate_entry = Entry(root)
rate_entry.pack()

# Time Period
Label(root, text="Time Period (Years):").pack()
time_entry = Entry(root)
time_entry.pack()

# Calculate Button
Button(root,
       text="Calculate",
       command=calculate_interest).pack(pady=10)

# Result Label
result_label = Label(root, text="")
result_label.pack()

# Run Application
root.mainloop()