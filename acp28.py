# =====================================
# ACTIVITY 51: Area and Perimeter of Circle
# =====================================

import math

# Create Circle class
class Circle:

    # Constructor
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate area
    def area(self):
        return math.pi * self.radius * self.radius

    # Method to calculate perimeter (circumference)
    def perimeter(self):
        return 2 * math.pi * self.radius

# Take radius as input
r = float(input("Enter the radius of the circle: "))

# Create object
c = Circle(r)

# Display results
print("Area of the Circle =", c.area())
print("Perimeter of the Circle =", c.perimeter())