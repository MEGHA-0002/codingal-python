# =====================================
# ACTIVITY 16: Trigonometric Values
# =====================================

import math

# Taking angle input from the user
angle = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
radian = math.radians(angle)

# Calculate trigonometric values
sin_value = math.sin(radian)
cos_value = math.cos(radian)
tan_value = math.tan(radian)

# Display results
print("Sin(", angle, ") =", sin_value)
print("Cos(", angle, ") =", cos_value)
print("Tan(", angle, ") =", tan_value)