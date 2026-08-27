Absolutely. Since you're a **JS developer**, I'll teach Python Conditions by directly mapping everything to JavaScript.

# Python Conditions — JS Developer Guide

Conditions are used when your program needs to make decisions.

In JavaScript:

```javascript
if (age >= 18) {
  console.log("Adult");
}
```

In Python:

```python
if age >= 18:
    print("Adult")
```

The concept is the same. The **syntax is different**.

---

# 1. `if`

### JavaScript

```javascript
const age = 25;

if (age >= 18) {
  console.log("Adult");
}
```

### Python

```python
age = 25

if age >= 18:
    print("Adult")
```

Notice three differences:

```text
JavaScript                    Python

if (condition) {              if condition:
    ...                           ...
}                             indentation
```

Python doesn't use:

- `()`
- `{}`
- `;`

Instead, Python uses `:` and indentation.

---

# 2. Indentation ⭐

This is probably the biggest syntax change you'll notice coming from JavaScript.

JavaScript:

```javascript
if (age >= 18) {
  console.log("Adult");
  console.log("Can vote");
}
```

Python:

```python
if age >= 18:
    print("Adult")
    print("Can vote")
```

The indentation tells Python:

> These statements belong to the `if` block.

This would be invalid:

```python
if age >= 18:
print("Adult")
```

You need indentation:

```python
if age >= 18:
    print("Adult")
```

Usually Python uses **4 spaces**.

---

# 3. `else`

### JavaScript

```javascript
const age = 15;

if (age >= 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}
```

### Python

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Very simple mapping:

```text
JS              Python

if              if
else            else
{ }             indentation
```

---

# 4. `elif` → JavaScript's `else if`

This is important.

### JavaScript

```javascript
if (score >= 80) {
  console.log("A+");
} else if (score >= 70) {
  console.log("A");
} else if (score >= 60) {
  console.log("B");
} else {
  console.log("Fail");
}
```

### Python

```python
score = 75

if score >= 80:
    print("A+")
elif score >= 70:
    print("A")
elif score >= 60:
    print("B")
else:
    print("Fail")
```

Python uses:

```python
elif
```

instead of:

```javascript
else if
```

### Remember:

```text
JavaScript          Python

else if             elif
```

---

# 5. Multiple Conditions

You learned operators already.

JavaScript:

```javascript
const age = 25;
const isActive = true;

if (age >= 18 && isActive) {
  console.log("Allowed");
}
```

Python:

```python
age = 25
is_active = True

if age >= 18 and is_active:
    print("Allowed")
```

Mapping:

```text
JS          Python

&&          and
||          or
!           not
```

---

# 6. `and`

Both conditions must be true.

```python
age = 25
is_active = True

if age >= 18 and is_active:
    print("User can access")
```

Think:

```text
age >= 18    → True
is_active    → True

True AND True → True
```

If either one is false:

```python
age = 25
is_active = False

if age >= 18 and is_active:
    print("User can access")
```

Nothing prints.

---

# 7. `or`

Only one condition needs to be true.

JavaScript:

```javascript
if (isAdmin || isManager) {
  console.log("Access granted");
}
```

Python:

```python
if is_admin or is_manager:
    print("Access granted")
```

Example:

```python
is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access granted")
```

Output:

```text
Access granted
```

---

# 8. `not`

JavaScript:

```javascript
if (!is_active) {
  console.log("User is inactive");
}
```

Python:

```python
if not is_active:
    print("User is inactive")
```

Example:

```python
is_active = False

if not is_active:
    print("User is inactive")
```

---

# 9. Comparison Operators

Conditions heavily use comparison operators.

```python
age = 25

if age == 25:
    print("Age is 25")
```

Available:

```text
==      Equal
!=      Not equal
>       Greater than
<       Less than
>=      Greater than or equal
<=      Less than or equal
```

### Important JS difference

JavaScript:

```javascript
age === 25;
```

Python:

```python
age == 25
```

Python doesn't use `===`.

---

# 10. Python Chained Conditions ⭐

This is a really nice Python feature.

In JavaScript:

```javascript
if (age >= 18 && age <= 60) {
  console.log("Working age");
}
```

Python can write:

```python
if 18 <= age <= 60:
    print("Working age")
```

Example:

```python
age = 30

if 18 <= age <= 60:
    print("Working age")
```

This is equivalent to:

```python
if age >= 18 and age <= 60:
    print("Working age")
```

Python's chained comparison is very useful.

---

# 11. `in` in Conditions

Python's `in` operator is extremely useful.

Suppose:

```python
category = "Food"

if category in ["Food", "Transport", "Bills"]:
    print("Valid category")
```

JavaScript equivalent:

```javascript
const category = "Food";

if (["Food", "Transport", "Bills"].includes(category)) {
  console.log("Valid category");
}
```

So:

```text
JavaScript                       Python

array.includes(value)            value in array
```

---

# 12. `not in`

Python:

```python
category = "Shopping"

if category not in ["Food", "Transport", "Bills"]:
    print("Other category")
```

JavaScript equivalent:

```javascript
if (!["Food", "Transport", "Bills"].includes(category)) {
  console.log("Other category");
}
```

---

# 13. `is None`

This is very common in Python backend development.

JavaScript:

```javascript
if (user === null) {
  console.log("User not found");
}
```

Python:

```python
if user is None:
    print("User not found")
```

Example:

```python
user = None

if user is None:
    print("User not found")
```

Output:

```text
User not found
```

Remember:

```text
Python:

None → null-like value
is None → commonly used to check it
```

---

# 14. Truthy / Falsy

Python has truthy and falsy values, just like JavaScript.

### Falsy values

```python
False
None
0
0.0
""
[]
{}
set()
```

Example:

```python
name = ""

if not name:
    print("Name is empty")
```

JavaScript:

```javascript
const name = "";

if (!name) {
  console.log("Name is empty");
}
```

Very similar.

---

# 15. Checking a List

Suppose your expense list is:

```python
expenses = []
```

You can do:

```python
if expenses:
    print("Expenses available")
else:
    print("No expenses")
```

Because an empty list is falsy.

JavaScript equivalent:

```javascript
if (expenses.length > 0) {
  console.log("Expenses available");
} else {
  console.log("No expenses");
}
```

⚠️ This is an important difference.

In JavaScript:

```javascript
if ([]) {
  console.log("true");
}
```

An empty array is **truthy**.

In Python:

```python
if []:
    print("true")
```

An empty list is **falsy**.

---

# 16. Nested Conditions

JavaScript:

```javascript
if (user) {
  if (user.isActive) {
    console.log("User is active");
  }
}
```

Python:

```python
if user:
    if user["isActive"]:
        print("User is active")
```

You can also simplify it:

```python
if user and user["isActive"]:
    print("User is active")
```

---

# 17. Expense Tracker Example

Let's apply conditions to the project you're building.

```python
amount = 500

if amount > 1000:
    print("High expense")
elif amount > 500:
    print("Medium expense")
else:
    print("Small expense")
```

For:

```python
amount = 500
```

Output:

```text
Small expense
```

Because:

```text
500 > 1000 → False
500 > 500  → False
else       → True
```

---

# 18. Expense Validation

This is more realistic for your FastAPI application.

```python
amount = 500
category = "Food"

if amount <= 0:
    print("Invalid amount")

elif category not in ["Food", "Transport", "Bills", "Shopping"]:
    print("Invalid category")

else:
    print("Expense is valid")
```

Flow:

```text
amount <= 0?
      ↓
     No
      ↓
category valid?
      ↓
     Yes
      ↓
Expense is valid
```

---

# 19. Authentication Example

Since you're a backend developer, this pattern will be very familiar.

### JavaScript

```javascript
if (!user) {
  return res.status(404).json({
    message: "User not found",
  });
}

if (!user.isActive) {
  return res.status(403).json({
    message: "User is inactive",
  });
}

console.log("Access granted");
```

Python/FastAPI:

```python
if user is None:
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

if not user["isActive"]:
    raise HTTPException(
        status_code=403,
        detail="User is inactive"
    )

print("Access granted")
```

You'll use this kind of condition constantly in backend development.

---

# 20. Ternary Operator

JavaScript:

```javascript
const status = age >= 18 ? "Adult" : "Minor";
```

Python has a different syntax:

```python
status = "Adult" if age >= 18 else "Minor"
```

Example:

```python
age = 25

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output:

```text
Adult
```

### Remember this syntax:

```python
value_if_true if condition else value_if_false
```

---

# 21. JS vs Python — Ternary

```text
JavaScript:

condition ? true_value : false_value


Python:

true_value if condition else false_value
```

This feels strange initially, but you'll get used to it quickly.

---

# 22. `match` — Python's Switch Alternative

JavaScript:

```javascript
switch (category) {
  case "Food":
    console.log("Food expense");
    break;

  case "Transport":
    console.log("Transport expense");
    break;

  default:
    console.log("Other");
}
```

Modern Python has `match`:

```python
match category:
    case "Food":
        print("Food expense")

    case "Transport":
        print("Transport expense")

    case _:
        print("Other")
```

Think:

```text
JavaScript switch       Python match
case                    case
default                 case _
```

You don't need to master `match` immediately. Learn `if/elif/else` first.

---

# 23. Python Condition Cheat Sheet

Keep this:

```text
JavaScript                         Python
──────────────────────────────────────────────

if (age >= 18) {                   if age >= 18:
    ...
}

else {                             else:
    ...
}

else if (...) {                    elif ...:

&&                                 and
||                                 or
!                                  not

===                                ==
!==                                !=

array.includes(x)                 x in array
!array.includes(x)                x not in array

value === null                     value is None

condition ? a : b                  a if condition else b

switch                             match
```

---

# 🧠 The Most Important Python Condition Rules

As a JS developer, focus on these **7 things**:

### 1. No parentheses required

```python
if age >= 18:
```

### 2. Colon is required

```python
if age >= 18:
```

### 3. Indentation defines the block

```python
if age >= 18:
    print("Adult")
```

### 4. `elif` = `else if`

```python
elif age >= 13:
```

### 5. `and/or/not`

```python
if age >= 18 and is_active:
```

### 6. `==` instead of JS's `===`

```python
if age == 18:
```

### 7. `is None`

```python
if user is None:
```

---

# 🎯 Practice

Try converting these **JS conditions to Python** without looking at the answers.

### Exercise 1

```javascript
const age = 25;

if (age >= 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}
```

---

### Exercise 2

```javascript
const score = 75;

if (score >= 80) {
  console.log("A+");
} else if (score >= 70) {
  console.log("A");
} else if (score >= 60) {
  console.log("B");
} else {
  console.log("Fail");
}
```

---

### Exercise 3

Convert this:

```javascript
const age = 25;
const isActive = true;

if (age >= 18 && isActive) {
  console.log("Access granted");
}
```

---

### Exercise 4 — Expense Tracker

Write Python for:

```text
amount = 1500

If amount >= 1000:
    print "High expense"

Else if amount >= 500:
    print "Medium expense"

Otherwise:
    print "Low expense"
```

### Exercise 5 — Backend

Write Python for:

```text
user = None

If user is missing:
    raise HTTPException 404
Otherwise:
    print "User found"
```

These five exercises will make the transition from **JavaScript conditions → Python conditions** much faster.
