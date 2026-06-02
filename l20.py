# =====================================
# ACTIVITY 18: Current Date and Time
# =====================================

import datetime
import random

now = datetime.datetime.now()

print("Current Date and Time:")
print(now)


# =====================================
# ACTIVITY 19: Random Date
# =====================================

year = random.randint(2000, 2030)
month = random.randint(1, 12)
day = random.randint(1, 28)

random_date = datetime.date(year, month, day)

print("\nRandom Date:")
print(random_date)


# =====================================
# ACTIVITY 20: Trip Expenditure Calculator
# =====================================

transport = float(input("\nEnter transport cost: "))
food = float(input("Enter food cost: "))
accommodation = float(input("Enter accommodation cost: "))
other = float(input("Enter other expenses: "))

total = transport + food + accommodation + other

print("\nTotal Trip Expenditure =", total)