Absolutely. Since you already know JavaScript, let's learn **Python Loops by mapping them directly to JavaScript**.

# Python Loops — JS Developer Guide

Loops are used when you want to repeat code.

For example, in JavaScript:

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

Python gives you a different style:

```python
for i in range(5):
    print(i)
```

The concept is the same, but Python's syntax is much simpler.

---

# 1. `for` Loop

## JavaScript

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

Output:

```text
0
1
2
3
4
```

## Python

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

### Important difference

JavaScript:

```javascript
i++;
```

Python doesn't have `i++`.

Instead, Python's `range()` handles the iteration.

---

# 2. Understanding `range()`

`range()` is extremely important in Python.

```python
range(5)
```

means:

```text
0
1
2
3
4
```

It stops **before 5**.

So:

```python
for i in range(5):
    print(i)
```

means:

```text
start = 0
stop = 5
step = 1
```

---

# 3. `range(start, stop)`

JavaScript:

```javascript
for (let i = 1; i < 5; i++) {
  console.log(i);
}
```

Python:

```python
for i in range(1, 5):
    print(i)
```

Output:

```text
1
2
3
4
```

Think:

```text
range(start, stop)
```

`stop` is excluded.

---

# 4. `range(start, stop, step)`

JavaScript:

```javascript
for (let i = 0; i < 10; i += 2) {
  console.log(i);
}
```

Python:

```python
for i in range(0, 10, 2):
    print(i)
```

Output:

```text
0
2
4
6
8
```

So:

```python
range(start, stop, step)
```

Example:

```python
range(0, 10, 2)
```

means:

```text
start → 0
stop  → 10
step  → 2
```

---

# 5. Loop Through an Array → List

This is where Python becomes very nice.

### JavaScript

```javascript
const fruits = ["Apple", "Banana", "Mango"];

for (const fruit of fruits) {
  console.log(fruit);
}
```

### Python

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

That's it.

No:

```text
const
of
{}
```

Python simply says:

```python
for fruit in fruits:
```

---

# 6. This Is Very Important for You

Because you're working with FastAPI and JSON, you'll constantly do this:

```python
expenses = [
    {
        "id": 1,
        "title": "Lunch",
        "amount": 250
    },
    {
        "id": 2,
        "title": "Uber",
        "amount": 380
    }
]

for expense in expenses:
    print(expense["title"])
```

Output:

```text
Lunch
Uber
```

In JavaScript:

```javascript
for (const expense of expenses) {
  console.log(expense.title);
}
```

Very similar conceptually.

---

# 7. Loop Through Dictionary

Suppose:

```python
user = {
    "name": "Gowtam",
    "age": 30,
    "role": "Developer"
}
```

### Loop keys

```python
for key in user:
    print(key)
```

Output:

```text
name
age
role
```

This is roughly like:

```javascript
for (const key in user) {
  console.log(key);
}
```

---

# 8. Loop Through Dictionary Values

Python:

```python
for value in user.values():
    print(value)
```

Output:

```text
Gowtam
30
Developer
```

JavaScript equivalent:

```javascript
for (const value of Object.values(user)) {
  console.log(value);
}
```

---

# 9. Loop Through Key + Value

This is very common in Python.

```python
for key, value in user.items():
    print(key, value)
```

Output:

```text
name Gowtam
age 30
role Developer
```

JavaScript:

```javascript
for (const [key, value] of Object.entries(user)) {
  console.log(key, value);
}
```

### Remember

```text
Python                         JavaScript

dict.keys()                    Object.keys()
dict.values()                  Object.values()
dict.items()                   Object.entries()
```

---

# 10. `while` Loop

Python's `while` loop is very similar to JavaScript.

### JavaScript

```javascript
let count = 0;

while (count < 5) {
  console.log(count);
  count++;
}
```

### Python

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Output:

```text
0
1
2
3
4
```

Important:

Python doesn't have:

```python
count++
```

Use:

```python
count += 1
```

---

# 11. `break`

`break` is almost exactly the same.

JavaScript:

```javascript
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break;
  }

  console.log(i);
}
```

Python:

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

Output:

```text
0
1
2
3
4
```

---

# 12. `continue`

Again, almost identical.

JavaScript:

```javascript
for (let i = 0; i < 5; i++) {
  if (i === 2) {
    continue;
  }

  console.log(i);
}
```

Python:

```python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

Output:

```text
0
1
3
4
```

---

# 13. `pass` — Python Specific

Python has something called:

```python
pass
```

It means:

> Do nothing for now.

Example:

```python
for i in range(5):
    if i == 2:
        pass

    print(i)
```

It's useful when Python requires a statement but you don't want to implement anything yet.

For example:

```python
def process_expense():
    pass
```

This is similar to temporarily having an empty function body.

In JavaScript:

```javascript
function processExpense() {
  // TODO
}
```

---

# 14. `enumerate()` ⭐

This is one of the most useful Python features for a JS developer.

Suppose:

```python
expenses = ["Lunch", "Uber", "Shopping"]
```

You want both:

```text
index
value
```

Python:

```python
for index, expense in enumerate(expenses):
    print(index, expense)
```

Output:

```text
0 Lunch
1 Uber
2 Shopping
```

JavaScript:

```javascript
expenses.forEach((expense, index) => {
  console.log(index, expense);
});
```

Python equivalent:

```python
for index, expense in enumerate(expenses):
    print(index, expense)
```

---

# 15. Start `enumerate()` From 1

Very useful when displaying lists.

```python
expenses = ["Lunch", "Uber", "Shopping"]

for index, expense in enumerate(expenses, start=1):
    print(index, expense)
```

Output:

```text
1 Lunch
2 Uber
3 Shopping
```

---

# 16. Loop With `range()` and List Index

You can do:

```python
expenses = ["Lunch", "Uber", "Shopping"]

for i in range(len(expenses)):
    print(expenses[i])
```

This works.

But Python developers generally prefer:

```python
for expense in expenses:
    print(expense)
```

And if you need the index:

```python
for i, expense in enumerate(expenses):
    print(i, expense)
```

### Rule of thumb

Don't unnecessarily use:

```python
range(len(items))
```

Prefer:

```python
for item in items:
```

or:

```python
for index, item in enumerate(items):
```

---

# 17. Nested Loops

JavaScript:

```javascript
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    console.log(i, j);
  }
}
```

Python:

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

Output:

```text
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

Again, indentation defines the nesting.

---

# 18. Loop + Condition

This combination is extremely important.

Suppose:

```python
expenses = [
    {"title": "Lunch", "amount": 250},
    {"title": "Laptop", "amount": 50000},
    {"title": "Uber", "amount": 380}
]
```

Find expensive expenses:

```python
for expense in expenses:
    if expense["amount"] > 1000:
        print(expense["title"])
```

Output:

```text
Laptop
```

JavaScript:

```javascript
for (const expense of expenses) {
  if (expense.amount > 1000) {
    console.log(expense.title);
  }
}
```

This pattern will be everywhere in your FastAPI application.

---

# 19. Find an Expense by ID

This directly connects to the code you were writing earlier.

```python
expense_id = 2

for expense in expenses:
    if expense["id"] == expense_id:
        print(expense)
        break
```

This means:

```text
Loop through expenses
        ↓
Check ID
        ↓
Found?
   ↓          ↓
 YES          NO
  ↓            ↓
return/break  continue
```

This is essentially what you were doing in:

```python
for expense in data["expenses"]:
    if expense["id"] == expense_id:
        return expense
```

---

# 20. `for ... else` ⭐

Python has a feature that may look strange initially.

```python
expenses = [
    {"id": 1, "title": "Lunch"},
    {"id": 2, "title": "Uber"}
]

expense_id = 5

for expense in expenses:
    if expense["id"] == expense_id:
        print(expense)
        break
else:
    print("Expense not found")
```

Output:

```text
Expense not found
```

The `else` runs when the loop finishes **without hitting `break`**.

This is different from a normal `if/else`.

For backend code, you'll often see this pattern, although you don't have to use it.

---

# 21. List Comprehension ⭐⭐⭐

This is one of the most important Python concepts after basic loops.

Suppose you want numbers from 1–5.

Normal loop:

```python
numbers = []

for i in range(1, 6):
    numbers.append(i)
```

Python allows:

```python
numbers = [i for i in range(1, 6)]
```

Output:

```text
[1, 2, 3, 4, 5]
```

This is called a:

**List comprehension**

---

# 22. JS `map()` vs Python List Comprehension

JavaScript:

```javascript
const numbers = [1, 2, 3, 4, 5];

const doubled = numbers.map((n) => n * 2);
```

Python:

```python
numbers = [1, 2, 3, 4, 5]

doubled = [n * 2 for n in numbers]
```

Output:

```text
[2, 4, 6, 8, 10]
```

Think:

```text
JavaScript map()        Python list comprehension
```

---

# 23. JS `filter()` vs Python Comprehension

JavaScript:

```javascript
const numbers = [1, 2, 3, 4, 5];

const result = numbers.filter((n) => n > 3);
```

Python:

```python
numbers = [1, 2, 3, 4, 5]

result = [n for n in numbers if n > 3]
```

Output:

```text
[4, 5]
```

This syntax is very powerful.

---

# 24. Expense Tracker Example

Suppose:

```python
expenses = [
    {"title": "Lunch", "amount": 250},
    {"title": "Laptop", "amount": 50000},
    {"title": "Uber", "amount": 380},
    {"title": "Shopping", "amount": 3000}
]
```

### Normal loop

```python
high_expenses = []

for expense in expenses:
    if expense["amount"] > 1000:
        high_expenses.append(expense)
```

### List comprehension

```python
high_expenses = [
    expense
    for expense in expenses
    if expense["amount"] > 1000
]
```

Result:

```python
[
    {"title": "Laptop", "amount": 50000},
    {"title": "Shopping", "amount": 3000}
]
```

---

# 25. Loop Cheat Sheet

Keep this mapping:

```text
JavaScript                         Python
──────────────────────────────────────────────

for (let i = 0; i < 5; i++)        for i in range(5):

for (const item of items)          for item in items:

for (const key in obj)             for key in obj:

Object.entries(obj)                obj.items()

items.forEach(...)                 for item in items:

items.map(...)                     [x for x in items]

items.filter(...)                  [x for x in items if ...]

break                               break

continue                            continue

while (condition)                  while condition:

i++                                i += 1

i--                                i -= 1

```

---

# 🧠 Most Important Things for You

As a JS developer, learn these first:

### Level 1 — Must Know

```python
for item in items:
    print(item)
```

```python
for i in range(10):
    print(i)
```

```python
while condition:
    ...
```

```python
break
continue
```

### Level 2 — Very Important

```python
for index, item in enumerate(items):
    print(index, item)
```

```python
for key, value in data.items():
    print(key, value)
```

### Level 3 — Python Power

```python
result = [x * 2 for x in numbers]
```

```python
result = [x for x in numbers if x > 10]
```

---

# 🎯 Practice for You

Try these without looking at the answers.

### Exercise 1 — Basic

Convert this JS:

```javascript
for (let i = 1; i <= 10; i++) {
  console.log(i);
}
```

---

### Exercise 2 — Array

Convert:

```javascript
const fruits = ["Apple", "Banana", "Mango"];

for (const fruit of fruits) {
  console.log(fruit);
}
```

---

### Exercise 3 — Filter

Given:

```python
numbers = [10, 20, 5, 30, 7, 40]
```

Print only numbers greater than `20`.

---

### Exercise 4 — Expense

Given:

```python
expenses = [
    {"id": 1, "title": "Lunch", "amount": 250},
    {"id": 2, "title": "Laptop", "amount": 50000},
    {"id": 3, "title": "Uber", "amount": 380},
    {"id": 4, "title": "Shopping", "amount": 3000}
]
```

Print only expenses where:

```text
amount > 1000
```

---

### Exercise 5 — Find by ID

Write a loop that finds:

```text
expense_id = 3
```

and returns the matching expense.

This last exercise is particularly important because it's almost exactly the pattern you're already using in your **FastAPI expense tracker**.
