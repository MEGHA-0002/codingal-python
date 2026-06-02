# =====================================
# ACTIVITY 21: List Operations
# =====================================

# Create an empty list
empty_list = []
print("Empty List:", empty_list)

# A list of numbers
numbers = [1, 2, 3, 4, 5]
print("Numbers List:", numbers)

# Use * operator
triples = [1, 2, 3] * 3
print("Triples List:", triples)

# Reverse the given list
aList = [100, 200, 300, 400, 500]
aList = aList[::-1]
print("Reversed List:", aList)


# =====================================
# ACTIVITY 22: Match Words
# =====================================

# Function to check whether first and last
# character of words match

def match_words(words):
    ctr = 0
    lst = []

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("\nList of words with first and last character same:")
    print(lst)

    return ctr

count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])

print("Number of words having first and last character same:", count)


# =====================================
# ACTIVITY 23: Sum, Average, Largest and Smallest
# =====================================

L = [4, 5, 1, 2, 9, 7, 10, 8]

print("\nOriginal List:", L)

# Variable to store the sum
count = 0

# Finding the sum
for i in L:
    count += i

# Calculating average
avg = count / len(L)

print("Sum =", count)
print("Average =", avg)

# Sorting the list
L.sort()

# Printing smallest and largest elements
print("Smallest element is:", L[0])
print("Largest element is:", L[-1])