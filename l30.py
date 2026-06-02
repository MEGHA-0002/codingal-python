# =====================================
# ACTIVITY 56: Private Variables and Methods
# =====================================

class MyClass:

    # Private variable
    __privateVar = 27

    # Private method
    def __privMeth(self):
        print("I'm inside class MyClass")

    # Public method to access private members
    def hello(self):
        print("Private Variable value:", MyClass.__privateVar)
        self.__privMeth()

# Object creation
foo = MyClass()
foo.hello()


# =====================================
# ACTIVITY 57: Encapsulation Using Setter Method
# =====================================

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# Attempt to change private variable directly
c.__maxprice = 1000
c.sell()

# Change price using setter method
c.setMaxPrice(1000)
c.sell()


# =====================================
# ACTIVITY 58: String Representation of an Object
# =====================================

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Method to print points in coordinate format
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

# Object creation
p1 = Point(2, 3)
print(p1)