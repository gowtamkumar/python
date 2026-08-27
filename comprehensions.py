numbers = [1, 2, 3, 4, 5]
# Comprehension Without Condition
result = []
for number in numbers:
    result.append(number * 3)
print(result)
# Comprehension With Condition
res_com = [number * 3 for number in numbers]

print(res_com)

names = ["gowtam", "rahul", "amit"]

upper_names = [name.upper() for name in names]

print(upper_names)


even_odd = [number * 2 for number in numbers if number % 2 == 0]

print(even_odd)

expenses = [
    {"id": 1, "title": "Lunch", "amount": 250},
    {"id": 2, "title": "Uber", "amount": 380},
    {"id": 3, "title": "Laptop", "amount": 50000},
    {"id": 4, "title": "Shopping", "amount": 3000},
]

title = [expense["title"] for expense in expenses]

print(title)

# Conditional transformation:
# [value_if_true if condition else value_if_false for x in numbers]
show_string = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print(show_string)

# Nested Loops in Comprehension
numbers = [1, 2, 3]
letters = ["A", "B"]

result = []

for number in numbers:
    for letter in letters:
        result.append((number, letter))

res = [(number, latter) for number in numbers for latter in letters]

print(res)

# Nested List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rest = [number for row in matrix for number in row]

print(rest)

# Set Comprehension
numbers = [1, 2, 2, 3, 3, 4]

unique = {number for number in numbers}

print(unique)
# Generator Expression

numbers = [1, 2, 3, 4, 5]

result = [number * 2 for number in numbers]

# sum() + Comprehension
expenses = [
    {"title": "Lunch", "amount": 250},
    {"title": "Uber", "amount": 380},
    {"title": "Shopping", "amount": 3000},
]


total = sum(expense["amount"] for expense in expenses)

print("total", total)
