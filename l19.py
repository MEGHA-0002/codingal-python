# =====================================
# ACTIVITY 13: Number Guessing Game
# =====================================

import random

playing = True
number = str(random.randint(0, 9))

print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you win!")

while playing:
    guess = input("Give me your best guess!\n")

    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("Your guess isn't quite right, try again.\n")


# =====================================
# ACTIVITY 14: Rock Paper Scissors Game
# =====================================

import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")

    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")

    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")

    if play_again != "y":
        break


# =====================================
# ACTIVITY 15: Mathematical Operations
# =====================================

import math

# Using ceil() and floor()
print("The Floor and Ceiling value of 23.56 are:",
      math.floor(23.56), "and", math.ceil(23.56))

x = 10
y = -15

# Using copysign()
print("The value of x after copying the sign from y is:",
      math.copysign(x, y))

# Using fabs()
print("Absolute value of -96 is:", math.fabs(-96))
print("Absolute value of 56 is:", math.fabs(56))

# Using gcd()
print("The GCD of 24 and 56 is:", math.gcd(24, 56))