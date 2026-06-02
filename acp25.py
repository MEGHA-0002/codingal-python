# =====================================
# ACTIVITY 42: List Comprehension Practice
# =====================================

# Create a list of numbers from 1 to 10
numbers = [x for x in range(1, 11)]

print("Numbers:", numbers)

# Square of each number
squares = [x**2 for x in numbers]
print("Squares:", squares)

# Even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)

# Odd numbers
odd_numbers = [x for x in numbers if x % 2 != 0]
print("Odd Numbers:", odd_numbers)