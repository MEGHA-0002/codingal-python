# Program to calculate the circumference of a circle

def circumference(radius):
    return 2 * 3.14 * radius

# Taking input from the user
r = float(input("Enter the radius of the circle: "))

# Calculating and displaying the circumference
print("The circumference of the circle is:", circumference(r))