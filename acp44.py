# =====================================
# ACTIVITY 75: Rock Paper Scissors App
# =====================================

from tkinter import *
import random

# Function to play the game
def play(user_choice):

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"

    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"Your Choice: {user_choice}\n"
             f"Computer Choice: {computer_choice}\n"
             f"Result: {result}"
    )

# Create Window
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Heading
Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 16)
).pack(pady=10)

# Instruction
Label(
    root,
    text="Choose Rock, Paper or Scissors"
).pack()

# Buttons
Button(
    root,
    text="Rock",
    width=10,
    command=lambda: play("Rock")
).pack(pady=5)

Button(
    root,
    text="Paper",
    width=10,
    command=lambda: play("Paper")
).pack(pady=5)

Button(
    root,
    text="Scissors",
    width=10,
    command=lambda: play("Scissors")
).pack(pady=5)

# Result Label
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run Application
root.mainloop()