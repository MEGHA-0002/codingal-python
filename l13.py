# ==========================================
# Activity 1: Half Pyramid Pattern of Stars
# Objective: Print a half pyramid pattern using stars (*).
# ==========================================

print("Half Pyramid Pattern of Stars (*)")
n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(i + 1):
        print("* ", end="")
    print()


# ==========================================
# Activity 2: Floyd's Triangle
# Objective: Print Floyd's Triangle using numbers.
# ==========================================

rows = int(input("Please Enter the Total Number of Rows: "))
number = 1

print("Floyd's Triangle")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end="  ")
        number = number + 1
    print()


# ==========================================
# Activity 3: Diamond Number Pattern
# Objective: Print a diamond-shaped number pattern.
# ==========================================

rowSize = int(input("Enter the number of rows: "))

if rowSize % 2 == 0:
    halfDiamRow = int(rowSize / 2)
else:
    halfDiamRow = int(rowSize / 2) + 1

space = halfDiamRow - 1

# Upper Part
for i in range(1, halfDiamRow + 1):
    for j in range(1, space + 1):
        print(end=" ")

    space = space - 1
    num = 1

    for j in range(2 * i - 1):
        print(end=str(num))
        num = num + 1

    print()

# Lower Part
space = 1

for i in range(1, halfDiamRow):
    for j in range(1, space + 1):
        print(end=" ")

    space = space + 1
    num = 1

    for j in range(1, 2 * (halfDiamRow - i)):
        print(end=str(num))
        num = num + 1

    print()