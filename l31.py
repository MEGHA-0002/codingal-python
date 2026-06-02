# =====================================
# ACTIVITY 60: Abstract Class Example
# =====================================

from abc import ABC, abstractmethod

# Create base class
class Absclass(ABC):

    def print(self, x):
        print("Passed value:", x)

    @abstractmethod
    def task(self):
        pass

# Create subclass
class TestClass(Absclass):

    def task(self):
        print("We are inside TestClass task")

# Object creation
test_obj = TestClass()

test_obj.task()
test_obj.print(100)


# =====================================
# ACTIVITY 61: Abstract Method Example
# =====================================

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):

    def move(self):
        print("I can crawl")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):

    def move(self):
        print("I can roar")

# Object creation
Human().move()
Snake().move()
Dog().move()
Lion().move()


# =====================================
# ACTIVITY 62: Polymorphism Example
# =====================================

class India:

    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA:

    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

# Object creation
obj_ind = India()
obj_usa = USA()

# Common Interface
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
    print()