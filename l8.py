# ==========================================
# Lesson 8 - Operator Precedence and Applications
# ==========================================

# ==========================================
# Activity 1: Operator Precedence
# ==========================================

v = 4
w = 5
x = 8
y = 2

result = (v + w) * x / y

print("Value of (v + w) * x / y is", result)

name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")


# ==========================================
# Activity 2: Divisibility Checker
# ==========================================

print("\nEnter a Number (Numerator):")
numerator = int(input())

print("Enter a Number (Denominator):")
denominator = int(input())

if numerator % denominator == 0:
    print(str(numerator) + " is divisible by " + str(denominator))
else:
    print(str(numerator) + " is not divisible by " + str(denominator))


# ==========================================
# Activity 3: Mean Value Calculator
# ==========================================

mean1 = 38
wrong_number = 36
correct_number = 56
total_numbers = 40

# Sum based on incorrect mean

total_sum = mean1 * total_numbers
print("The sum of 40 numbers:", total_sum)

# Corrected sum

correct_sum = total_sum - wrong_number + correct_number
print("Corrected sum:", correct_sum)

# Correct mean

mean2 = correct_sum / total_numbers
print("Correct Mean =", mean2)
