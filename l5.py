# ==========================================
# Lesson 5 - Conditional Statements
# ==========================================

# ==========================================
# Activity 1: Conditional Statements
# ==========================================

num = 3

if num > 0:
    print(num, "is a positive number.")

num = -1

if num > 0:
    print(num, "is a positive number.")


# ==========================================
# Activity 2: Profit or Loss Calculator
# ==========================================

actual_cost = float(input("\nPlease Enter the Actual Product Price: "))
sale_amount = float(input("Please Enter the Sales Amount: "))

if sale_amount > actual_cost:
    profit = sale_amount - actual_cost
    print("Total Profit =", profit)
else:
    print("No Profit!")


# ==========================================
# Activity 3: Odd or Even Checker
# ==========================================

number = int(input("\nEnter a Number: "))

print("Number to be checked:", number)

if number % 2 == 0:
    print("This is an Even Number")
else:
    print("This is an Odd Number")
