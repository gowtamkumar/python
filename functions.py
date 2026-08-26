def add(a, b):
    return a + b


result = add(40, 22)
print(result)


def greet():
    return "Hello, World!"


print(greet())


def print_expense(amount):
    print(f"Expense amount: {amount}")


print_expense(100)


def calculate_area(len, wid):
    return len, wid


len, wid = calculate_area(5, 10)
print(f"Length: {len}, Width: {wid}")


# def get_user():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     return {"name": name, "age": age}


# # name, age = get_user()
# user_info = get_user()
# print(user_info["age"])


def add(a: int, b: int) -> int:
    return a + b


# argument
def add_all(*args):
    print(args)  # Output: (1, 2, 3, 4, 5)
    total = 0
    for num in args:
        total += num
    return total


print(add_all(1, 2, 3, 4, 5))  # Output: 15


def create_user(**data):
    print(data)


create_user(
    name="John", age=30, city="New York"
)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}


def example(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


example(1, 2, 3, name="Alice", age=25)

name = "John"


def greet_user():
    print(f"Hello, {name}!")


greet_user()  # Output: Hello, John!

# counter
counter = 0


def increment_counter():
    global counter
    counter += 1
    print(f"Counter: {counter}")


increment_counter()
increment_counter()
increment_counter()
increment_counter()
increment_counter()


print(counter)  # Output: 5

# Nested Functions


def outer_function():
    print("This is then outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()


outer_function()  # Output: This is the outer function. This is the inner function.


# Passing Function as Argument
def greet_user1():
    print("Hello, User!")


def execute_function(func):
    func()


execute_function(greet_user1)  # Output: Hello, User!

# Lambda Functions
add_lambda = lambda x, y: x + y
print(add_lambda(40, 20))
# Lambda + map()
numbers = [1, 2, 3, 45, 5]

result = list(map(lambda x: x * 2, numbers))
print(result)

total_result = [x * 2 for x in result]
print(total_result)

# Docstrings


def calculation_total(price, quantity):
    """
    calculate the total price
    args:
      price: product price
      qty:number of product

    Returns:
      total price.
    """
    return price * quantity


print(calculation_total(10, 30))


# | JavaScript             | Python               |
# | ---------------------- | -------------------- |
# | `function`             | `def`                |
# | `function add(a,b)`    | `def add(a,b):`      |
# | `{}`                   | indentation          |
# | `return`               | `return`             |
# | `...args`              | `*args`              |
# | object arguments       | `**kwargs`           |
# | default params         | default params       |
# | `=>`                   | `lambda`             |
# | `obj.method()`         | `obj.method()`       |
# | `=== null`             | `is None`            |
# | TypeScript `: number`  | Python `: int/float` |
# | TypeScript return type | Python `-> type`     |
