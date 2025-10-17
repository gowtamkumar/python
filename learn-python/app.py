import math

# variable
students_count = 100
rating = 4.99
is_published = True
couser_name = " python programming "

# string
couser = """
  hi john
  how old are you boss?
"""

print(f"{couser_name}")

print(len(couser))
print(couser_name[1])
print(couser_name[0:-1])
print(couser_name[0:])
print(couser_name[:3])
print(couser_name[:])
niche = 'hello "paython"'
exm = 'python "programming'
exm1 = "python \nprogramming"
print(exm1)
# format string
first = "Gowtam"
last = "Kumar"
full = first + " " + last
full1 = f"{first} {last}"
full2 = f"{len(first)} {last} {60 + 2}"
print(full)
print(full1)
print(full2)
# string method
print(couser_name.upper())
print(couser_name.capitalize())
print(couser_name.lower())
print(couser_name.title())
# whitchspace remove
print(couser_name.strip())
# find specific character
print(couser_name.find("Pro"))
# replace specific character
print(couser_name.replace("p", "j"))
# find then return boolean
print("pro" in couser_name)
# find then return boolean
print("swif" not in couser_name)

# number
print("---------------here down show number--------------------")
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
# floting number remove
print(10 // 3)
print(10 % 3)
# here borgo calcuation
print(2**3)

# x = x + 1 and x += 4 same
x = 4
x = x + 1
x += 4
print(x)

#  module
print(math.ceil(3.3))


# building fun
print(round(3.5))
# here abs can be remove -
print(abs(-3.9))

# y = input("x: ")
# z = input("z: ")
# here all time input is string type
# so you can convert this sting
#  int()
#  float()
#  bool() this boolean
#  str()

# print(int(y) + int(z))
# print(float(y))
# # boolean
# print(bool(y))
# print(type(str(y)))

# Falsy list

# print(bool(0))        # Output: False
# print(bool(""))       # Output: False
# print(bool(None))     # Output: False

# truthy value

# print(bool(1))        # Output: True
# print(bool("hello"))  # Output: True
# print(bool([1, 2]))   # Output: True

# fundamentals fo programming
# comparison operators
# >
# <
# >=
# ==

temperature = 40
if temperature < 0:
    print("its warm")
    print("drink water")
elif temperature > 11:
    print("this learn elif condition")
else:
    print("its cold")
print("this condition is full")

# ternary operator
age = 22
# if age >= 10:
#   message = "Eligible"
# else:
#   message = "Not eligible"
# up if contiond can be convet by ternary oprator
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# logical operators
# and
# or
# not

hight_income = True
good_credit = True
student = False
if hight_income and good_credit:
    print("Eligible condition")
else:
    print("not eligible")

if hight_income or good_credit:
    print("Eligible condition")
else:
    print("not eligible")

if not student:
    print("Eligible")
else:
    print("Not eligible")
if (hight_income or good_credit) and not student:
    print("this condition is Eligible")
else:
    print("this condigtion is not eligible")

# Chaning comparision operators
# age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    print("Eligible")
if 18 <= age < 65:
    print("Chaning comparision operators")


# loop
# for loop
for number in range(1, 90):
    print("this only loop", number)

# for loop  range start, end else with break
successfull = False
for number in range(2, 10):
    print("Attempt", number, number * ".")
    if successfull:
        print("Successfull")
        break
else:
    print("Attenmpted 3 time and failed")

# nested loop

for x in range(2, 3):
    for y in range(20, 22):
        print(f"({x}, {y})")

print(type(3))
print(type(range(5)))


# Iterable
for z in "learn python":
    print(z)
