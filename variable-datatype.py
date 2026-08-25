print("Hello, World!")
NAME = "Gowtam kumar"
age = 23
price = 300.6

print("my name is " + NAME + " and my age is " + str(age))


valo = True
kharp = False

name = '"Gowtam kumar"'
print(name)

print(isinstance(age, int))
print(isinstance(price, float))

user = None
print(user)
print(type(user))


if user is not None:
    print("user is not None")

fruits = ["apple", "banana", "cherry"]
print(fruits[0])

fruits.append("orange")
print(fruits)


user = {"name": "Gowtam kumar", "age": 23, "is_active": True}

print(user["name"])


user["payment"] = 300.6
print(user)
# tuple
user3 = ("gowtam", 32)

print(user3)

# set
numbers = {1, 2, 3, 4, 5}
print(numbers)


role = "33"
print(type(role))
print(isinstance(role, str))

print(type(str(33)))

if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
