# =========================
# Activity 1: Create a Basic Window
# =========================

from tkinter import *

# Create Window
window = Tk()

# Set the window Title and Geometry
window.title("Demo Window")
window.geometry("400x300")

# Start the GUI event loop
window.mainloop()
# =========================
# Activity 2: Getting Started with Widgets
# =========================

from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

# Add Label
lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=30)

# Add Label and Entry Widget
name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

# Function to display a message
def display():
    name = name_entry.get()
    
    greet = "Hello " + name + "\n"
    message = "Welcome to the Application!\n"
    today = "Today's date is: " + str(date.today())

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, today)

# Text Widget
text_box = Text(height=5)

# Button
btn = Button(text="Begin", command=display,
             height=1, bg="#1261A0", fg="white")

# Arrange Widgets
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

# Start GUI event loop
root.mainloop()