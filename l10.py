# ==========================================
# Activity 1: Sum of First N Numbers
# Objective: Calculate the sum of numbers from 1 to n using a for loop.
# ==========================================

n = int(input("Enter the number whose sum you want to find: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)


# ==========================================
# Activity 2: Reverse a String
# Objective: Reverse a string entered by the user using a for loop.
# ==========================================

string = input("Please enter your own String: ")

string2 = ""

for i in string:
    string2 = i + string2

print("\nThe Original String =", string)
print("The Reversed String =", string2)


# ==========================================
# Activity 3: Print Numbers in Reverse Order
# Objective: Print numbers from n to 1 using a for loop.
# ==========================================

n = int(input("Enter the value of n: "))

print("Numbers from {0} to {1} are:".format(n, 1))

for i in range(n, 0, -1):
    print(i)