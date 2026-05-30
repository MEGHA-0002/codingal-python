# ==========================================
# Activity: Mirrored Right-Angled Triangle
# Objective: Print a mirrored right-angled triangle pattern using stars (*).
# ==========================================

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    
    for k in range(i):
        print("*", end="")
    
    print()