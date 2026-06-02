# =====================================
# ACTIVITY 68: Warning Message Box
# =====================================

from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.title("Virus Scanner")
root.geometry("200x200")

# Function to display warning message
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

# Add button
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

root.mainloop()


# =====================================
# ACTIVITY 69: Event Handling
# =====================================

from tkinter import *

# Create window
window = Tk()
window.title("Event Handler")
window.geometry("200x100")

# Event handler for key press
def handle_keypress(event):
    print("Key Pressed:", event.char)

# Bind key press event
window.bind("<Key>", handle_keypress)

# Event handler for button click
def handle_click(event):
    print("The button was clicked!")

# Create button
button = Button(window, text="Click Me!")
button.pack()

# Bind click event
button.bind("<Button-1>", handle_click)

# Start GUI
window.mainloop()