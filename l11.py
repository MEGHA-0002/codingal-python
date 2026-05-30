# ==========================================
# Activity 1: Sum of First N Numbers Using While Loop
# Objective: Calculate the sum of numbers from 1 to n using a while loop.
# ==========================================

n = int(input("Enter the value of terms: "))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)


# ==========================================
# Activity 2: Infinite Loop
# Objective: Demonstrate how an infinite loop works using a while loop.
# ==========================================

i = 0

while i <= 0:
    print("I WILL RUN FOREVER")


# ==========================================
# Activity 3: Armstrong Number Checker
# Objective: Check whether a given number is an Armstrong number.
# ==========================================

num = int(input("Enter a number: "))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")