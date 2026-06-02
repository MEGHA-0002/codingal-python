# =====================================
# ACTIVITY 25: Tuple Creation and Modification
# =====================================

# Create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print("Tuple with different data types:", tuplex)

# Create a tuple
tuplex = (4, 6, 2, 8, 3, 1)
print("Original Tuple:", tuplex)

# Tuples are immutable, so adding an element creates a new tuple
tuplex = tuplex + (9,)
print("Tuple after adding an element:", tuplex)


# =====================================
# ACTIVITY 26: Tuple Palindrome (Flip-Flop)
# =====================================

def palind(r):
    e = len(r) - 1
    s = 0

    while s < e:
        if r[s] != r[e]:
            return False
        s += 1
        e -= 1

    return True

r = (1, 2, 3, 3, 2, 1)

if palind(r):
    print("The Tuple is Flip-Flop")
else:
    print("The Tuple is not Flip-Flop")


# =====================================
# ACTIVITY 27: Tuple Count and Slicing
# =====================================

tuple1 = (50, 10, 60, 70, 50)

# Count occurrences of 50
print("Count of 50:", tuple1.count(50))

# Create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

# Slicing
_slice = tuplex[3:5]
print("Tuple slice [3:5]:", _slice)

_slice = tuplex[:6]
print("Tuple slice [:6]:", _slice)


# =====================================
# ACTIVITY 28: Weather Analysis
# =====================================

weather = (1, 0, 0, 0, 1, 1, 0)

sunny = 0
rainy = 0

for i in range(0, 7):
    if weather[i] == 0:
        rainy += 1
    else:
        sunny += 1

if sunny > rainy:
    print("Good weather")
else:
    print("Bad weather")