Absolutely. Since you already know **JavaScript**, let's learn **Python Functions by comparing them directly with JavaScript**.

Functions are extremely important because in your FastAPI project you'll use them everywhere:

```python
def get_expenses():
    ...

def save_expenses(data):
    ...

def create_expense(expense):
    ...
```

---

# 1. What is a Function?

A function is a reusable block of code that performs a specific task.

### JavaScript

```javascript
function add(a, b) {
  return a + b;
}

const result = add(10, 20);

console.log(result);
```

### Python

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

The basic mapping is:

```text
JavaScript                 Python

function                   def
{ }                        indentation
return                     return
```

---

# 2. Creating a Function

### JavaScript

```javascript
function sayHello() {
  console.log("Hello");
}
```

### Python

```python
def say_hello():
    print("Hello")
```

Notice:

```python
def say_hello():
```

The `:` is required.

And the function body is determined by indentation.

---

# 3. Calling a Function

### JavaScript

```javascript
sayHello();
```

### Python

```python
say_hello()
```

Python doesn't need `;`.

---

# 4. Function With Parameters

Parameters are values that a function receives.

### JavaScript

```javascript
function greet(name) {
  console.log(`Hello ${name}`);
}

greet("Gowtam");
```

### Python

```python
def greet(name):
    print(f"Hello {name}")

greet("Gowtam")
```

Output:

```text
Hello Gowtam
```

---

# 5. Multiple Parameters

JavaScript:

```javascript
function add(a, b) {
  return a + b;
}
```

Python:

```python
def add(a, b):
    return a + b
```

Call:

```python
result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

# 6. `return`

`return` works almost exactly the same as JavaScript.

### JavaScript

```javascript
function calculateTotal(price, quantity) {
  return price * quantity;
}
```

### Python

```python
def calculate_total(price, quantity):
    return price * quantity
```

Then:

```python
total = calculate_total(100, 3)

print(total)
```

Output:

```text
300
```

---

# 7. Function Without `return`

Python functions don't have to return anything.

```python
def print_expense(amount):
    print(f"Expense: {amount}")
```

Calling:

```python
print_expense(500)
```

Output:

```text
Expense: 500
```

Technically, Python returns:

```python
None
```

if you don't explicitly use `return`.

For example:

```python
def test():
    print("Hello")

result = test()

print(result)
```

Output:

```text
Hello
None
```

---

# 8. Multiple Values From a Function ⭐

This is an important Python feature.

You can return multiple values:

```python
def get_user():
    name = "Gowtam"
    age = 30

    return name, age
```

Then:

```python
name, age = get_user()

print(name)
print(age)
```

Output:

```text
Gowtam
30
```

Python internally returns these as a tuple.

Conceptually:

```python
return (name, age)
```

---

# 9. JavaScript Equivalent

JavaScript usually does:

```javascript
function getUser() {
  return {
    name: "Gowtam",
    age: 30,
  };
}

const { name, age } = getUser();
```

Python:

```python
def get_user():
    return {
        "name": "Gowtam",
        "age": 30
    }

user = get_user()

print(user["name"])
```

Or:

```python
name, age = get_user()
```

if the function returns multiple values directly.

---

# 10. Default Parameters

Very similar to JavaScript.

### JavaScript

```javascript
function greet(name = "Guest") {
  console.log(`Hello ${name}`);
}
```

Python:

```python
def greet(name="Guest"):
    print(f"Hello {name}")
```

Now:

```python
greet()
```

Output:

```text
Hello Guest
```

And:

```python
greet("Gowtam")
```

Output:

```text
Hello Gowtam
```

---

# 11. Keyword Arguments ⭐

Python has a very useful feature called **keyword arguments**.

```python
def create_expense(title, amount, category):
    print(title)
    print(amount)
    print(category)
```

You can call:

```python
create_expense(
    title="Lunch",
    amount=250,
    category="Food"
)
```

The order doesn't matter when using keyword arguments:

```python
create_expense(
    category="Food",
    amount=250,
    title="Lunch"
)
```

This is very useful in Python backend code.

---

# 12. Positional vs Keyword Arguments

### Positional

```python
create_expense("Lunch", 250, "Food")
```

Python matches based on position:

```text
title     → Lunch
amount    → 250
category  → Food
```

### Keyword

```python
create_expense(
    title="Lunch",
    amount=250,
    category="Food"
)
```

Python matches based on parameter name.

---

# 13. Type Hints ⭐⭐⭐

Since you're a **TypeScript/JavaScript backend developer**, you'll probably love Python type hints.

Basic Python:

```python
def add(a, b):
    return a + b
```

With type hints:

```python
def add(a: int, b: int) -> int:
    return a + b
```

This means:

```text
a       → int
b       → int
return  → int
```

This will feel similar to TypeScript:

```typescript
function add(a: number, b: number): number {
  return a + b;
}
```

---

# 14. Python vs TypeScript

### TypeScript

```typescript
function getTotal(price: number, quantity: number): number {
  return price * quantity;
}
```

### Python

```python
def get_total(
    price: float,
    quantity: int
) -> float:
    return price * quantity
```

Very similar concept.

---

# 15. Type Hints Don't Work Exactly Like TypeScript

Important:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Python generally doesn't enforce these annotations at runtime.

For example:

```python
add("Hello", "World")
```

Python can still execute it and produce:

```text
HelloWorld
```

Type hints are primarily for:

- IDEs
- static analysis
- documentation
- developer tooling
- frameworks such as FastAPI

FastAPI makes especially heavy use of Python's type annotations.

---

# 16. Function With Optional Value

You can use:

```python
def greet(name: str | None = None):
    if name is None:
        name = "Guest"

    print(f"Hello {name}")
```

Then:

```python
greet()
```

Output:

```text
Hello Guest
```

And:

```python
greet("Gowtam")
```

Output:

```text
Hello Gowtam
```

For Python 3.12, this syntax is perfectly valid:

```python
str | None
```

---

# 17. `*args`

This is where Python functions become more interesting.

Suppose you don't know how many positional arguments will be passed.

```python
def add_all(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

Now:

```python
print(add_all(10, 20))
print(add_all(10, 20, 30))
print(add_all(1, 2, 3, 4, 5))
```

Output:

```text
30
60
15
```

`*args` collects positional arguments into a tuple.

Conceptually:

```python
add_all(10, 20, 30)
```

becomes:

```python
numbers = (10, 20, 30)
```

---

# 18. JavaScript Equivalent of `*args`

JavaScript uses rest parameters:

```javascript
function addAll(...numbers) {
  let total = 0;

  for (const number of numbers) {
    total += number;
  }

  return total;
}
```

Python:

```python
def add_all(*numbers):
    ...
```

So:

```text
JavaScript     Python

...numbers     *numbers
```

---

# 19. `**kwargs`

Python also has:

```python
**kwargs
```

This collects arbitrary keyword arguments.

Example:

```python
def create_user(**data):
    print(data)
```

Call:

```python
create_user(
    name="Gowtam",
    age=30,
    role="Developer"
)
```

Output:

```python
{
    "name": "Gowtam",
    "age": 30,
    "role": "Developer"
}
```

So:

```text
*args      → positional arguments
**kwargs   → keyword arguments
```

---

# 20. JavaScript Equivalent

JavaScript:

```javascript
function createUser(data) {
  console.log(data);
}

createUser({
  name: "Gowtam",
  age: 30,
  role: "Developer",
});
```

Python:

```python
def create_user(**data):
    print(data)
```

Call:

```python
create_user(
    name="Gowtam",
    age=30,
    role="Developer"
)
```

---

# 21. `*args` + `**kwargs`

You can use both:

```python
def example(*args, **kwargs):
    print(args)
    print(kwargs)
```

Call:

```python
example(
    10,
    20,
    30,
    name="Gowtam",
    role="Developer"
)
```

Output conceptually:

```text
(10, 20, 30)

{
    "name": "Gowtam",
    "role": "Developer"
}
```

You don't need to use these everywhere. Learn them after normal functions are comfortable.

---

# 22. Scope — Local Variables

This is important.

```python
def test():
    message = "Hello"

    print(message)

test()
```

`message` exists inside the function.

Trying:

```python
print(message)
```

outside the function will cause an error.

This is similar to JavaScript's function scope.

---

# 23. Global Variables

Example:

```python
name = "Gowtam"

def greet():
    print(name)

greet()
```

Output:

```text
Gowtam
```

The function can read the global variable.

But avoid unnecessarily relying on global mutable state in backend applications.

---

# 24. `global`

Python has a `global` keyword.

```python
count = 0

def increment():
    global count
    count += 1

increment()

print(count)
```

Output:

```text
1
```

But in production backend applications, it's generally better to avoid global mutable state when you can.

---

# 25. Nested Functions

Python allows functions inside functions.

```python
def outer():

    def inner():
        print("Inside inner")

    inner()

outer()
```

Output:

```text
Inside inner
```

JavaScript also supports this:

```javascript
function outer() {
  function inner() {
    console.log("Inside inner");
  }

  inner();
}
```

---

# 26. Functions Are First-Class Objects ⭐⭐⭐

This is very important if you know JavaScript.

You can assign a function to a variable.

Python:

```python
def greet():
    print("Hello")

hello = greet

hello()
```

Output:

```text
Hello
```

JavaScript:

```javascript
function greet() {
  console.log("Hello");
}

const hello = greet;

hello();
```

Exactly the same concept.

---

# 27. Passing Function as Argument

Python:

```python
def greet():
    print("Hello")


def execute(function):
    function()


execute(greet)
```

Output:

```text
Hello
```

JavaScript:

```javascript
function greet() {
  console.log("Hello");
}

function execute(fn) {
  fn();
}

execute(greet);
```

This is extremely important for understanding:

- callbacks
- decorators
- higher-order functions
- FastAPI dependencies
- middleware concepts

---

# 28. Lambda Functions

Python has anonymous functions called `lambda`.

JavaScript:

```javascript
const add = (a, b) => a + b;
```

Python:

```python
add = lambda a, b: a + b
```

Then:

```python
print(add(10, 20))
```

Output:

```text
30
```

However, Python developers generally prefer a normal `def` when the function becomes more complex.

---

# 29. Lambda + `map()`

Python:

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

Output:

```text
[2, 4, 6, 8]
```

But Python's list comprehension is usually cleaner:

```python
result = [x * 2 for x in numbers]
```

As a beginner, prioritize list comprehensions over excessive `lambda` usage.

---

# 30. Docstrings

Python functions can contain documentation.

```python
def calculate_total(price, quantity):
    """
    Calculate the total price.

    Args:
        price: Product price.
        quantity: Number of products.

    Returns:
        Total price.
    """
    return price * quantity
```

This is called a **docstring**.

It's commonly used in professional Python projects.

---

# 31. Your Expense Tracker — Functions

Now let's connect everything to your current project.

You might have:

```python
def get_expenses():
    ...
```

For example:

```python
def get_expenses():
    with open("expenses.json", "r") as file:
        return json.load(file)
```

Then:

```python
data = get_expenses()

print(data)
```

---

# 32. `save_expenses()`

```python
def save_expenses(data):
    with open("expenses.json", "w") as file:
        json.dump(data, file, indent=4)
```

Then:

```python
data = get_expenses()

data["expenses"].append(new_expense)

save_expenses(data)
```

This is a good example of why functions are useful:

```text
get_expenses()
       ↓
Read JSON

save_expenses()
       ↓
Write JSON
```

Instead of repeating file-handling code everywhere.

---

# 33. Function for Finding Expense

Your previous code was:

```python
for expense in data["expenses"]:
    if expense["id"] == expense_id:
        return expense
```

We can extract that into a function:

```python
def find_expense(expenses, expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            return expense

    return None
```

Then:

```python
expense = find_expense(data["expenses"], expense_id)

if expense is None:
    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )

return expense
```

This is a very important backend pattern:

```text
Route
  ↓
Service / Function
  ↓
Data
```

---

# 34. FastAPI + Function

Your route itself is also a function:

```python
@app.get("/view-expenses/{expense_id}")
def view_expense(expense_id: int):
    ...
```

FastAPI calls your function when the request arrives.

Conceptually:

```text
HTTP GET
   ↓
/view-expenses/1
   ↓
FastAPI
   ↓
view_expense(1)
   ↓
return response
```

So you've already been using Python functions—you just need to understand the underlying syntax now.

---

# 35. Type Hints + FastAPI ⭐⭐⭐

This:

```python
@app.get("/view-expenses/{expense_id}")
def view_expense(expense_id: int):
    ...
```

has:

```python
expense_id: int
```

This tells FastAPI:

> `expense_id` should be an integer.

And:

```python
def get_expense(expense_id: int) -> dict:
```

means:

```text
Input:
expense_id → int

Return:
dict
```

This is where Python functions + type hints become especially powerful for your backend work.

---

# 36. Default Parameter + Type Hint

You can combine them:

```python
def get_expenses(limit: int = 10):
    ...
```

Meaning:

```text
limit → int
default → 10
```

Call:

```python
get_expenses()
```

uses:

```text
limit = 10
```

Or:

```python
get_expenses(20)
```

uses:

```text
limit = 20
```

---

# 37. A Professional Expense Function

Putting several concepts together:

```python
def calculate_expense_total(
    expenses: list[dict]
) -> float:

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total
```

Then:

```python
total = calculate_expense_total(data["expenses"])

print(total)
```

This is the kind of function structure you'll see in real Python backend projects.

---

# 38. Function Naming — Python Style

As a JS developer, you may be used to:

```javascript
getExpenses();
calculateTotal();
createExpense();
```

Python usually follows **snake_case**:

```python
get_expenses()
calculate_total()
create_expense()
```

### Python convention

```python
def get_user_by_id():
    ...

def calculate_order_total():
    ...

def save_expense():
    ...
```

Use `snake_case` for functions and variables.

---

# 39. Python Function Cheat Sheet

Keep this:

```text
Create function:

def add(a, b):
    return a + b


Call:

add(10, 20)


Default parameter:

def greet(name="Guest"):
    ...


Type hints:

def add(a: int, b: int) -> int:
    ...


Keyword arguments:

add(a=10, b=20)


Multiple return:

return name, age


Variable positional arguments:

def test(*args):
    ...


Variable keyword arguments:

def test(**kwargs):
    ...


Anonymous function:

lambda x: x * 2
```

---

# 🧠 JS → Python Function Mapping

| JavaScript             | Python               |
| ---------------------- | -------------------- |
| `function`             | `def`                |
| `function add(a,b)`    | `def add(a,b):`      |
| `{}`                   | indentation          |
| `return`               | `return`             |
| `...args`              | `*args`              |
| object arguments       | `**kwargs`           |
| default params         | default params       |
| `=>`                   | `lambda`             |
| `obj.method()`         | `obj.method()`       |
| `=== null`             | `is None`            |
| TypeScript `: number`  | Python `: int/float` |
| TypeScript return type | Python `-> type`     |

---

# 🎯 What You Should Practice Now

Because your goal is to learn Python quickly from your existing JS knowledge, I'd practice these in order:

### Exercise 1 — Basic

Write:

```python
def greet(name):
    ...
```

Expected:

```text
greet("Gowtam")
→ Hello Gowtam
```

### Exercise 2 — Calculator

Create:

```python
add()
subtract()
multiply()
divide()
```

Each should accept two numbers and return the result.

### Exercise 3 — Expense

Create:

```python
def calculate_total(expenses):
    ...
```

Given:

```python
expenses = [
    {"title": "Lunch", "amount": 250},
    {"title": "Uber", "amount": 300},
    {"title": "Shopping", "amount": 1000}
]
```

Expected:

```text
1550
```

### Exercise 4 — Find Expense

Create:

```python
def find_expense(expenses, expense_id):
    ...
```

It should return the expense if found, otherwise:

```python
None
```

### Exercise 5 — FastAPI

Create:

```python
@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    ...
```

This will connect everything you've learned so far:

**variables → data types → operators → conditions → loops → functions → FastAPI.**
