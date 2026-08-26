fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")
# Change an Item
fruits[1] = "kola"
print(fruits)
# insert()
fruits.insert(1, "Banana")

# print(fruits)

# fruits.remove("kola")
# print(fruits)

# fruits.pop(1)
# print(fruits)

# last = fruits.pop()
# print(last)
# print(fruits)

# List Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[0:3])
print(numbers[1:3])
# Slice With Step
print(fruits[::2])
# Reverse a List
print(numbers[::-1])
numbers.reverse()

print(numbers)

# sort
number_sort = [5, 2, 8, 1, 3]
# num_sort = number_sort.sort()
# print(number_sort)

# # sort descending
# number_sort.sort(reverse=True)
# print(number_sort)


print(sorted(number_sort))
print(number_sort)

# List + List
a = [1, 2]
b = [3, 4]

result = b + a

print(result)

# List Repetition
numbers = [1, 2]

print(numbers * 3)
numbers = [1, 2]

# Dictionary
user = {"name": "Gowtam", "age": 30, "role": "Developer"}
# Change Dictionary Value
user["age"] = 31
# Add New Property
user["email"] = "gowtam@example.com"
# Delete Property

del user["email"]

# get
print(user.get("name"))

print(user.get("email", "No email"))

# Dictionary Keys
print(user.keys())
# Dictionary Keys
user = {"name": "Gowtam", "address": {"city": "Jessore", "country": "Bangladesh"}}

print(user["address"]["city"])

expenses = [
    {"id": 1, "title": "Lunch", "amount": 250, "category": "Food"},
    {"id": 2, "title": "Uber", "amount": 380, "category": "Transport"},
    {"id": 3, "title": "Shopping", "amount": 3000, "category": "Shopping"},
]

for expense in expenses:
    print(expense["title"])
# Dictionary Comprehension
numbers = [1, 2, 3, 4]

squeres = {number: number**2 for number in numbers}
print(squeres)

# Copying Lists — Important
a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)
b = a.copy()
b.append(4)
print(a)
print(b)

# Dictionary Copy
user = {
    "name": "Gowtam",
    "age": 44,
}

new_user = user.copy()

new_user["age"] = 32

print(user)
print(new_user)

# | JavaScript            | Python                        |
# | --------------------- | ----------------------------- |
# | `Array`               | `list`                        |
# | `Object`              | `dict`                        |
# | `arr.push(x)`         | `arr.append(x)`               |
# | `arr.pop()`           | `arr.pop()`                   |
# | `arr.length`          | `len(arr)`                    |
# | `arr.includes(x)`     | `x in arr`                    |
# | `arr.splice()`        | `insert() / remove() / pop()` |
# | `arr.sort()`          | `arr.sort()`                  |
# | `arr.reverse()`       | `arr.reverse()`               |
# | `Object.keys(obj)`    | `obj.keys()`                  |
# | `Object.values(obj)`  | `obj.values()`                |
# | `Object.entries(obj)` | `obj.items()`                 |
# | `obj[key]`            | `obj[key]`                    |
# | `delete obj[key]`     | `del obj[key]`                |
# | `obj?.key`            | `obj.get("key")`              |
# | `arr.map()`           | list comprehension            |
# | `arr.filter()`        | list comprehension            |
# | `...arr`              | `*arr` / unpacking            |
