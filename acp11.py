# ==========================================
# Activity: Count Total Digits in a Number
# Objective: Calculate the total number of digits in a number entered by the user.
# ==========================================

num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count = count + 1

print("Total digits =", count)