# ==========================================
# Activity 1: Exam Eligibility Checker
# Objective: Check whether a student is allowed to attend the exam based on medical reasons or attendance percentage.
# ==========================================

medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()

if medical_cause == 'Y':
    print("You are allowed")
else:
    atten = int(input("Enter the attendance of the student: "))

    if atten >= 75:
        print("Allowed")
    else:
        print("Not allowed")


# ==========================================
# Activity 2: Electricity Bill Calculator
# Objective: Calculate the electricity bill based on the number of units consumed.
# ==========================================

units = int(input("Please enter Number of Units you Consumed: "))

if units < 50:
    amount = units * 2.60
    surcharge = 25

elif units <= 100:
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

elif units <= 200:
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45

else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

total = amount + surcharge
print("\nElectricity Bill = %.2f" % total)


# ==========================================
# Activity 3: Customize Your Ride
# Objective: Create a menu-driven program to select a vehicle and its type.
# ==========================================

print("Select your ride:")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("What type of bike?")
    print("1. Scooty")
    print("2. Scooter")

    choice2 = int(input("Enter your choice: "))

    if choice2 == 1:
        print("You have selected Scooty")
    else:
        print("You have selected Scooter")

elif choice == 2:
    print("What type of car?")
    print("1. Sedan")
    print("2. XUV")

    choice3 = int(input("Enter your choice: "))

    if choice3 == 1:
        print("You have selected Sedan")
    else:
        print("You have selected XUV")

else:
    print("Wrong choice!")