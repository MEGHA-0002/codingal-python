# ==========================================
# Lesson 7 - Special Operators in Python
# ==========================================

# ==========================================
# Activity 1: Identity Operator
# ==========================================

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)
print("a is c:", a is c)

print("a is not c:", a is not c)


# ==========================================
# Activity 2: Bitwise Operators
# ==========================================

a = 10
b = -10

# Right Shift Operator

print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)

# Left Shift Operator

a = 5
b = -10

print("a << 1 =", a << 1)
print("b << 1 =", b << 1)


# ==========================================
# Activity 3: Membership Operator
# ==========================================

print("\nEnter Marks Obtained in 5 Subjects:")

mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())

total = mark1 + mark2 + mark3 + mark4 + mark5
average = int(total / 5)

valid_range = range(0, 101)

if average not in valid_range:
    print("Invalid Input!")

elif average in range(91, 101):
    print("Your Grade is A1")

elif average in range(81, 91):
    print("Your Grade is A2")

elif average in range(71, 81):
    print("Your Grade is B1")

elif average in range(61, 71):
    print("Your Grade is B2")

elif average in range(51, 61):
    print("Your Grade is C1")

elif average in range(41, 51):
    print("Your Grade is C2")

elif average in range(33, 41):
    print("Your Grade is D")

elif average in range(21, 33):
    print("Your Grade is E1")

else:
    print("Your Grade is E2")
