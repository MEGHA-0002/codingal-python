# =====================================
# ACTIVITY 1: Weather Condition Program
# =====================================

def weather_condition():
    print("The weather is pleasant in:", spring)
    print("The weather is same in:", autumn)

spring = "autumn"
autumn = spring

weather_condition()


# =====================================
# ACTIVITY 2: Well Wishes Program
# =====================================

def well_wishes():
    print("hello")
    print("how are you?")

well_wishes()


# =====================================
# ACTIVITY 3: Calculator Program
# =====================================

def add(P, Q):
    return P + Q

def subtract(P, Q):
    return P - Q

def multiply(P, Q):
    return P * Q

def divide(P, Q):
    return P / Q

print("\nCalculator Program")
print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice (a/b/c/d): ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))

elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))

elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))

elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))

else:
    print("This is an invalid input")