# =====================================
# ACTIVITY 63: Vehicle Polymorphism
# =====================================

# Class BMW
class BMW:

    def fuel_type(self):
        print("BMW uses Petrol/Diesel")

    def max_speed(self):
        print("BMW maximum speed is 250 km/h")


# Class Ferrari
class Ferrari:

    def fuel_type(self):
        print("Ferrari uses Petrol")

    def max_speed(self):
        print("Ferrari maximum speed is 340 km/h")


# Object creation
car1 = BMW()
car2 = Ferrari()

# Polymorphism
for vehicle in (car1, car2):
    vehicle.fuel_type()
    vehicle.max_speed()
    print()