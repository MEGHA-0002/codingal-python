# =====================================
# ACTIVITY 44: Student Class
# =====================================

# Create a class
class Student:
    grade = 10
    print("Hi, I am a student of grade", grade)

# Create an object
ob = Student()


# =====================================
# ACTIVITY 45: Vehicle Class
# =====================================

class Vehicle:

    # Constructor
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Object creation
modelX = Vehicle(240, 18)

# Access instance variables
print("Model Max Speed:", modelX.max_speed)
print("Model Mileage:", modelX.mileage)


# =====================================
# ACTIVITY 46: Parrot Class
# =====================================

class Parrot:

    # Class attribute
    species = "bird"

    # Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create objects
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# Access class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# Access instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))