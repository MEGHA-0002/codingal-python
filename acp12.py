# ==========================================
# Activity: Decimal to Binary Conversion
# Objective: Convert a decimal number into its binary equivalent.
# ==========================================

decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)

print("Binary number =", binary[2:])