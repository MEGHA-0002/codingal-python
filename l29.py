# =====================================
# ACTIVITY 52: Single Inheritance - Vehicle and Bus
# =====================================

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)

print("Vehicle Name:", School_bus.name)
print("Speed:", School_bus.max_speed)
print("Mileage:", School_bus.mileage)


# =====================================
# ACTIVITY 53: Calling Parent Constructor
# =====================================

# Parent class
class Person:

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.idnumber)

# Child class
class Employee(Person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # Calling parent constructor
        Person.__init__(self, name, idnumber)

# Object creation
a = Employee('Rahul', 886012, 200000, "Intern")

# Calling parent class method
a.display()


# =====================================
# ACTIVITY 54: Inheritance with super()
# =====================================

# Parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# Child class
class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

# Object creation
peggy = Penguin()

peggy.whoisThis()
peggy.swim()
peggy.run()