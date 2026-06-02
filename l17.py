# =====================================
# ACTIVITY 5: Break Statement
# =====================================

# Take user input
a = input("Enter a word: ")

# Program to check break keyword
for i in a:
    if i == 'A':
        print("A is found")
        break
    else:
        print("A not found")


# =====================================
# ACTIVITY 6: Pass Statement
# =====================================

for x in range(10):
    if x % 20 == 0:
        print("twist")

    elif x % 15 == 0:
        pass

    elif x % 5 == 0:
        print("fizz")

    elif x % 3 == 0:
        print("buzz")

    else:
        print(x)


# =====================================
# ACTIVITY 7: Continue Statement
# =====================================

var = 10

while var > 0:
    var = var - 1

    if var == 5:
        continue

    print("\nCurrent variable value:", var)

print("\nGood bye!")