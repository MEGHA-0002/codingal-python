# =====================================
# ACTIVITY 48: String to Uppercase
# =====================================

class IOString:

    # Constructor
    def __init__(self):
        self.str1 = ""

    # Function to get input from user
    def get_String(self):
        self.str1 = input("Enter String: ")

    # Function to print string in uppercase
    def print_String(self):
        print("Result is:", self.str1.upper())

# Object creation
str1 = IOString()

# Call functions
str1.get_String()
str1.print_String()


# =====================================
# ACTIVITY 49: Constructor and Destructor
# =====================================

class Employee:

    # Constructor
    def __init__(self):
        print("Employee created")

    # Destructor
    def __del__(self):
        print("Destructor called")

def Create_obj():
    print("Making Object...")
    obj = Employee()
    print("Function end...")
    return obj

print("\nCalling Create_obj() function...")
obj = Create_obj()
print("Program End...")


# =====================================
# ACTIVITY 50: Pair Elements (Two Sum)
# =====================================

class PairElements:

    def twoSum(self, nums, target):

        # Create an empty dictionary
        lookup = {}

        # Iterate through the tuple
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)

            lookup[num] = i

# Take input from user
value = int(input("\nEnter sum for which you want to make this search: "))

print(
    "index1=%d, index2=%d"
    % PairElements().twoSum((10, 20, 30, 40, 50, 60, 70), value)
)