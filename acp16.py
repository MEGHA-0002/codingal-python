# =====================================
# ACTIVITY 4: Shutdown Function
# =====================================

def shutdown(command):
    if command == "yes":
        return "Shutting down..."
    elif command == "no":
        return "Shutdown aborted."
    else:
        return "Sorry, invalid input."

user_input = input("Do you want to shut down the system? (yes/no): ")
print(shutdown(user_input))