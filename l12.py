# ==========================================
# Activity 1: Count Total Digits in a Number
# Objective: Calculate the total number of digits in a number entered by the user.
# ==========================================

num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count = count + 1

print("Total digits =", count)


# ==========================================
# Activity 2: Prime Numbers in a Range
# Objective: Display all prime numbers between two numbers entered by the user.
# ==========================================

lower = int(input("Enter a lower range: "))
upper = int(input("Enter an upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


# ==========================================
# Activity 3: Product of Middle Digits
# Objective: Find the product of the middle two digits of a number having 4 or more digits.
# ==========================================

num = int(input("Enter the number: "))
t = num
numLen = 0

while t > 0:
    numLen = numLen + 1
    t = int(t / 10)

if numLen >= 4:
    numLen = int(numLen / 2)
    chk = 0

    while num > 0:
        rem = num % 10

        if chk == numLen:
            midOne = rem
        elif chk == (numLen - 1):
            midTwo = rem

        num = int(num / 10)
        chk = chk + 1

    prod = midOne * midTwo
    print("\nProduct of Mid digits (" + str(midOne) + " * " + str(midTwo) + ") =", prod)

else:
    print("\nIt's not a 4 or more than 4-digit number!")