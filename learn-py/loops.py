for k in range(10):
    print(k)

for i in range(1, 11):
    print(i)


for j in range(0, 10, 2):
    print(j)


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


expenses = [
    {"id": 1, "title": "Lunch", "amount": 250},
    {"id": 2, "title": "Uber", "amount": 380},
]

for expense in expenses:
    print(expense["title"])


user = {"name": "Gowtam", "age": 30, "role": "Developer"}

for key in user:
    print(user[key])

for key, value in user.items():
    print(key, value)

# while loop
counter = 0

while counter < 5:
    print(counter)
    counter += 1

# break
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)


for i in range(5):
    if i == 2:
        pass
    print(i)

# enumerate
expenses = ["Lunch", "Uber", "Shopping"]

for index, expense in enumerate(expenses):
    print(index, expense)

for index, expense in enumerate(expenses, start=1):
    print(index, expense)

# Loop With range() and List Index
print(len(expenses))


# nested loops
print("Nested Loops")
for i in range(5):
    for j in range(5):
        print(i, j)


expenses = [
    {"title": "Lunch", "amount": 250},
    {"title": "Laptop", "amount": 50000},
    {"title": "Uber", "amount": 380},
]

for expense in expenses:
    if expense["amount"] > 250:
        print(expense["title"], expense["amount"])

# List Comprehension
numbers = []

for i in range(1, 100):
    # if i % 2 == 0:
    numbers.append(i)

print(numbers)

# JS map() vs Python List Comprehension
numbers = [1, 2, 3, 4, 5]

doubled_numbers = [n * 2 for n in numbers]
print(doubled_numbers)

# JS filter() vs Python Comprehension

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)


expenses = [
    {"title": "Lunch", "amount": 250},
    {"title": "Laptop", "amount": 50000},
    {"title": "Uber", "amount": 380},
    {"title": "Shopping", "amount": 3000},
]

expense_filtered = [expense for expense in expenses if expense["amount"] > 500]
print(expense_filtered)


# JavaScript                         Python
# ──────────────────────────────────────────────

# for (let i = 0; i < 5; i++)        for i in range(5):

# for (const item of items)          for item in items:

# for (const key in obj)             for key in obj:

# Object.entries(obj)                obj.items()

# items.forEach(...)                 for item in items:

# items.map(...)                     [x for x in items]

# items.filter(...)                  [x for x in items if ...]

# break                               break

# continue                            continue

# while (condition)                  while condition:

# i++                                i += 1

# i--                                i -= 1
