# =====================================
# ACTIVITY 8: Customer Due Amount
# =====================================

# Taking input from the user
bill_amount = float(input("Enter the total bill amount: "))
paid_amount = float(input("Enter the amount paid by the customer: "))

# Calculating due amount
due_amount = bill_amount - paid_amount

# Displaying the result
if due_amount > 0:
    print("Customer due amount is:", due_amount)
elif due_amount == 0:
    print("Bill is fully paid.")
else:
    print("Excess amount paid:", abs(due_amount))