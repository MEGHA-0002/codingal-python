# ==========================================
# Lesson 6 - Logical Operators
# ==========================================

# ==========================================
# Activity 1: AND and OR Operators
# ==========================================

a = 10
b = 12
c = 0

# AND Operator
if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("At least one number has boolean value as False")

# OR Operator
a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("Either of the numbers is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the numbers is greater than 0")
else:
    print("No number is greater than 0")


# ==========================================
# Activity 2: Applications of Logical Operators
# ==========================================

a = 10
b = 12
c = 12

# NOT Operator
print(not (a == b))
print(not (b == c))

a = "python"
b = "coding"

if not (a == b):
    print(a, "and", b, "are different.")

a = 4
b = 5

if not ((a == 1) == (b == 5)):
    print("Hello")

num = int(input("\nEnter a number: "))

if not (num % 2 == 0):
    print(num, "is an odd number.")


# ==========================================
# Activity 3: BMI Checker
# ==========================================

height = float(input("\nEnter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height / 100) ** 2

print("Your BMI is", bmi)

if bmi <= 18.4:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are overweight.")
elif bmi <= 34.9:
    print("You are severely overweight.")
elif bmi <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")
