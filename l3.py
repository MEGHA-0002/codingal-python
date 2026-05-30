# ==========================================
# Lesson 3 - Data Types and Type Casting
# ==========================================

# ==========================================
# Activity 1: Data Types
# ==========================================

# Let's check the data type of different values

a = 5
print("Type of a:", type(a))

b = 2.5
print("Type of b:", type(b))

c = "coding"
print("Type of c:", type(c))

d = True
print("Type of d:", type(d))


# ==========================================
# Activity 2: Type Casting
# ==========================================

# Assigning different variables

name = "Penguin"
age = 15
is_student = True
weight = 38.5

# Printing variables and their data types

print("\nName:", name)
print("Data Type of Name is", type(name))

print("Age:", age)
print("Data Type of Age is", type(age))

print("Is Student:", is_student)
print("Data Type of Is Student is", type(is_student))

print("Weight:", weight)
print("Data Type of Weight is", type(weight))

# Type Casting

print("\nAfter Type Casting...")

age = str(age)
print(age)
print("Data Type of Age is", type(age))

weight = int(weight)
print(weight)
print("Data Type of Weight is", type(weight))


# ==========================================
# Activity 3: String Operations
# ==========================================

# Input a string

text = input("\nEnter a string: ")

# Reverse the string

reversed_text = text[::-1]

print("Reverse of the given string is:")
print(reversed_text)
