# =====================================
# ACTIVITY 1: Circumference of a Circle
# =====================================

def circumference(radius):
    return 2 * 3.14 * radius

r = float(input("Enter the radius of the circle: "))
print("The circumference of the circle is:", circumference(r))


# =====================================
# ACTIVITY 2: Cube of a Number if Divisible by 3
# =====================================

def cube(number):
    return number * number * number

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

print(by_three(9))
print(by_three(4))


# =====================================
# ACTIVITY 3: Factorial Using Recursion
# =====================================

def factorial(x):
    """This is a recursive function to find the factorial of an integer"""

    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial.__doc__)
print("The factorial of 0:", factorial(0))
print("The factorial of 1:", factorial(1))
print("The factorial of 2:", factorial(2))
print("The factorial of 5:", factorial(5))
print("The factorial of 10:", factorial(10))