# =====================================
# ACTIVITY 72: Top Level Window
# =====================================

from tkinter import *

# Main Window
root = Tk()
root.geometry("400x300")
root.title("Main Window")

# Function to open Top Level Window
def topwin():
    top = Toplevel()
    top.geometry("200x100")
    top.title("Top Level Window")

    label = Label(top, text="This is a Top Level Window")
    label.pack()

# Widgets in Main Window
label = Label(root, text="This is Root Window")
label.pack()

button = Button(
    root,
    text="Open Another Window",
    command=topwin
)
button.pack()

root.mainloop()