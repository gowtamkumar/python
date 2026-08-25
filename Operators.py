categoris = ["Electronics", "Clothing", "Books"]

find_cate = "Books"

if find_cate in categoris:
    print(f"{find_cate} category is available.")
else:
    print(f"{find_cate} category is not available.")
print(10 / 3)
print(10 // 3)
print(10 % 3)
# Comparison Operators
age = 25

print(age == 25)
print(age != 30)
print(age > 18)
print(age < 30)
print(age >= 25)
print(age <= 25)

# Logical Operators
# and
# or
# not
# is
is_active = False
if age >= 18 and is_active:
    print("User is an adult and active.")
else:
    print("User is either not an adult or not active.")

is_logged_in = True

if age >= 18 or is_logged_in:
    print("User is either an adult or logged in.")

if not is_active:
    print("User is not active.")

a = None
print(a is not None)
print(a is None)

c = 10
d = 20
print(c is d)
print(c == d)
# Membership Operators
# in
# not in

# Identity Operators
# is
# is not


# Bitwise Operators
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (Left Shift), >> (Right Shift)


# Operator Precedence

# Python Chained Comparisons
if 18 <= age <= 60:
    print("User is an adult.")

# String Operators
first_name = "Gowtam"
last_name = "Kumar"

full_name = first_name + " " + last_name

print(full_name)

# String repetition
print(full_name * 3)

# Truthy / Falsy
# False
# None
# 0
# 0.0
# ""
# []
# {}
# set()
