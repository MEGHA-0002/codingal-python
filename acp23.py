# =====================================
# ACTIVITY 33: Check the Frequency
# =====================================

# Initialize dictionary
test_dict = {
    'Codingal': 2,
    'is': 2,
    'best': 2,
    'for': 2,
    'Coding': 1
}

# Display original dictionary
print("Original Dictionary:", test_dict)

# Value whose frequency is to be checked
K = int(input("Enter the value to check frequency: "))

# Count frequency
frequency = 0

for key in test_dict:
    if test_dict[key] == K:
        frequency += 1

# Display result
print("Frequency of", K, "is:", frequency)