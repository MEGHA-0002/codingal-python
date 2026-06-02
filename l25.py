# =====================================
# ACTIVITY 39: Map and Lambda Functions
# =====================================

# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)

print("Addition of two lists:")
print(list(result))

# Using map to find squares
nums = [1, 2, 3, 4, 5]

def sq(n):
    return n * n

square = list(map(sq, nums))

print("Square of numbers in list:")
print(square)


# =====================================
# ACTIVITY 40: Zip Function Examples
# =====================================

# Zip elements of two sets
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}

s3 = list(zip(s1, s2))

print("\nZipped Sets:")
print(s3)

# Zip elements of two lists
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

print("\nElements using zip:")
for x, y in zip(list1, list2[::-1]):
    print(x, y)

# Zip into dictionary
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stock: price for stock, price in zip(stocks, prices)}

print("\nDictionary from zip:")
print(new_dict)


# =====================================
# ACTIVITY 41: Exit Function
# =====================================

for i in range(10):

    if i == 5:
        print("Program exited at i =", i)
        exit()

    print(i)