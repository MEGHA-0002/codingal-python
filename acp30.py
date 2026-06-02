# =====================================
# ACTIVITY 59: Class String Reverse
# =====================================

class ReverseString:

    def __init__(self, text):
        self.text = text

    # Method to reverse the string word by word
    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

# Take input from user
sentence = input("Enter a string: ")

# Create object
obj = ReverseString(sentence)

# Display reversed string
print("Reversed String:", obj.reverse_words())