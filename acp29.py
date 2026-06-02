# =====================================
# ACTIVITY 55: Bus Fare
# =====================================

# Parent Class
class Vehicle:

    def __init__(self, capacity):
        self.capacity = capacity

    # Calculate fare
    def fare(self):
        return self.capacity * 100


# Child Class
class Bus(Vehicle):

    # Total fare includes 10% maintenance charge
    def fare(self):
        amount = super().fare()
        total_fare = amount + (0.10 * amount)
        return total_fare


# Object Creation
school_bus = Bus(50)

# Display fare
print("Total Bus Fare:", school_bus.fare())