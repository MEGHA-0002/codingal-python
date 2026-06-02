# =====================================
# ACTIVITY 47: Dog Breed
# =====================================

# Create Dog class
class Dog:

    # Class variable
    animal = "Dog"

    # Constructor with two instance variables
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

# Create objects of different breeds
dog1 = Dog("Labrador", "Buddy")
dog2 = Dog("German Shepherd", "Rocky")

# Display details
print("Dog 1 Details")
print("Animal:", dog1.animal)
print("Breed:", dog1.breed)
print("Name:", dog1.name)

print("\nDog 2 Details")
print("Animal:", dog2.animal)
print("Breed:", dog2.breed)
print("Name:", dog2.name)