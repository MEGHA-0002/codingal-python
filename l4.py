# ==========================================
# Lesson 4 - Calculations in Python
# ==========================================

# ==========================================
# Activity 1: Average Calculation
# ==========================================

# Storing values

tree1 = 98
tree2 = 94
tree3 = 41
tree4 = 95
tree5 = 11

# Finding the total

total = tree1 + tree2 + tree3 + tree4 + tree5
print("The sum of all 5 trees is:", total)

# Finding the average

average = total / 5
print("The average of all 5 trees is:", average)


# ==========================================
# Activity 2: Count Currency Notes
# ==========================================

# Taking amount as input from the user

amount = int(input("\nPlease Enter Amount for Withdrawal: "))

# Calculating notes

note_100 = amount // 100
note_50 = (amount % 100) // 50
note_10 = ((amount % 100) % 50) // 10

print("Notes of 100 Rupees:", note_100)
print("Notes of 50 Rupees:", note_50)
print("Notes of 10 Rupees:", note_10)


# ==========================================
# Activity 3: Percentage Calculator
# ==========================================

print("\nEnter Marks Obtained in 4 Subjects:")

math = int(input("Maths: "))
english = int(input("English: "))
science = int(input("Science: "))
hindi = int(input("Hindi: "))

# Calculating total marks

total_marks = math + english + science + hindi
print("Total Marks =", total_marks)

# Calculating percentage

percentage = (total_marks / 400) * 100

print("Percentage Marks =", percentage)
