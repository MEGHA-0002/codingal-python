# Import necessary libraries
from tkinter import *
from datetime import date

# Create window
root = Tk()
root.title("Age Calculator")
root.geometry("350x300")

# Function to calculate age
def calculate_age():
    birth_day = int(day_entry.get())
    birth_month = int(month_entry.get())
    birth_year = int(year_entry.get())

    today = date.today()

    age = today.year - birth_year

    # Check if birthday has occurred this year
    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1

    result_label.config(text="Your Age is: " + str(age) + " years")

# Labels
Label(root, text="Enter Date of Birth", font=("Arial", 12)).pack(pady=10)

Label(root, text="Day").pack()
day_entry = Entry(root)
day_entry.pack()

Label(root, text="Month").pack()
month_entry = Entry(root)
month_entry.pack()

Label(root, text="Year").pack()
year_entry = Entry(root)
year_entry.pack()

# Button
Button(root, text="Calculate Age",
       command=calculate_age,
       bg="blue",
       fg="white").pack(pady=10)

# Result Label
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start GUI
root.mainloop()