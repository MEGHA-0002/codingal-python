# =====================================
# ACTIVITY 30: Remove Duplicate Values from Dictionary
# =====================================

student_data = {
    "id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (
        details["name"],
        details["class"],
        details["subject_integration"]
    )

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

print("Dictionary after removing duplicates:")
for k, v in result.items():
    print(k, ":", v)


# =====================================
# ACTIVITY 31: Frequency of a Value in Dictionary
# =====================================

test_dict = {
    'Codingal': 2,
    'is': 2,
    'best': 2,
    'for': 2,
    'Coding': 1
}

print("\nOriginal Dictionary:", test_dict)

K = 2

res = 0
for key in test_dict:
    if test_dict[key] == K:
        res += 1

print("Frequency of K is:", res)


# =====================================
# ACTIVITY 32: Dictionary Search Using get()
# =====================================

country_code = {
    'India': '0091',
    'Australia': '0025',
    'Nepal': '00977'
}

print("\nCountry code for India:")
print(country_code.get('India', 'Not Found'))

print("\nCountry code for Japan:")
print(country_code.get('Japan', 'Not Found'))