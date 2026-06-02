# =====================================
# ACTIVITY 43: Random Password Challenge
# =====================================

import random
import string

# Password length
length = 8

# Combine uppercase, lowercase, and digits
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Generate password
password = []

for i in range(length):
    password.append(random.choice(characters))

# Shuffle the password
random.shuffle(password)

# Convert list to string
password = "".join(password)

print("Generated Password:", password)