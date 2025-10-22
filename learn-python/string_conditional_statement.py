# single quotes, double quotes, or triple quotes (for multi‑line)
s1 = "hello python"
s2 = "hello python dubble quotes"
s3 = """hello python how old 
are you boss"""

print(s3)

# common opeations

# concatination
E_contatantion = s1 + " " + s2
print(E_contatantion)
# repetition string
E_repetition = s1 * 3
print(E_repetition)
# indexing
first_char = s1[0]
print(first_char)
# slicing
substring = s1[0:5]
print(substring)
# length
s_length = len(s3)
print(s_length)
# membership test
is_hello_in_s1 = "hello" in s1
print(is_hello_in_s1)
# uppercase and lowercase
upper_s1 = s1.upper()
print(upper_s1)
lowwer_case = s2.lower()
print(lowwer_case)
# stripping whitespace
s_with_spaces = "   hello world   "
stripped_s = s_with_spaces.strip()
print(stripped_s)
print(s_with_spaces)
# replacing
replaced_s = s1.replace("python", "Javasceript")
print(replaced_s)
# splitting
split_s = s1.split(" ")
print(split_s)
# joining
joined_s = "_".join(split_s)
print(joined_s)

# f-string (Python 3.6+)
name = "Alice"
age = 30
msg = f"{name} is {age} years old."
msg2 = "{} is {} years old.".format(name, age)
print(msg)
print(msg2)

is_ture = False

if is_ture:
    print("This is true")
elif not is_ture:
    print("This is false")
else:
    print("None of the above")


user_input = input("Enter a word: ")

if not user_input:
    print("You didn't type anything.")
elif user_input.isdigit():
    print("Thats a number, not a word.")
elif user_input.isalpha():
    print("this is all letters!")
else:
    print("Mixed characters.")

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("positive even number")
    else:
        print("positive odd number")
elif num < 0:
    print("nagative number")
else:
    print("Zero")


# ternary conditional operator
resutl = "even" if num % 2 == 0 else "odd"
print(f"This number is {resutl}")
