# =====================================
# ACTIVITY 34: Set Operations
# =====================================

# Set of integers
my_set = {1, 2, 3}
print("Set of integers:", my_set)

# Set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print("Set of mixed datatypes:", my_set)

# Set cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print("Set without duplicates:", my_set)

# Create a set from a list
my_set = set([1, 2, 3, 2])
print("Set created from list:", my_set)


# =====================================
# ACTIVITY 35: Remove an Element from a Set
# =====================================

num_set = set([0, 1, 3, 4, 5])

print("\nOriginal Set:")
print(num_set)

num_set.pop()

print("After removing an element:")
print(num_set)


# =====================================
# ACTIVITY 36: Intersection of Two Sets
# =====================================

setx = {"green", "blue"}
sety = {"blue", "yellow"}

print("\nOriginal Sets:")
print(setx)
print(sety)

setz = setx.intersection(sety)

print("Intersection of the two sets:")
print(setz)


# =====================================
# ACTIVITY 37: Array Operations
# =====================================

import array as arr

# Create an array
array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])

print("\nOriginal Array:")
print(array_num)

# Count occurrences of 3
print("Number of occurrences of 3:",
      array_num.count(3))

# Reverse the array
array_num.reverse()

print("Array after reversing:")
print(array_num)