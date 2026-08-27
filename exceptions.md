Absolutely. Since you're a **JavaScript/TypeScript developer**, Python Exceptions are easy if we directly compare them with `try/catch/throw`.

# Python Exceptions — JS Developer Guide

An **exception** is an error that happens while your program is running.

For example:

```python
number = 10
result = number / 0
```

This produces:

```text
ZeroDivisionError: division by zero
```

Instead of allowing the application to crash, we can **handle** the exception.

---

# 1. JavaScript vs Python

The biggest mapping is:

```text
JavaScript             Python

try                     try
catch                   except
finally                 finally
throw                   raise
Error                   Exception
```

### JavaScript

```javascript
try {
  // risky code
} catch (error) {
  // handle error
} finally {
  // always runs
}
```

### Python

```python
try:
    # risky code
except Exception as error:
    # handle error
finally:
    # always runs
```

The syntax is different, but the concept is almost identical.

---

# 2. Basic `try / except`

Python:

```python
try:
    number = 10 / 0
except:
    print("Something went wrong")
```

Output:

```text
Something went wrong
```

JavaScript:

```javascript
try {
  const number = 10 / 0;
} catch (error) {
  console.log("Something went wrong");
}
```

---

# 3. Don't Use Bare `except` in Production ⚠️

You can write:

```python
try:
    risky_operation()
except:
    print("Error")
```

But generally prefer:

```python
try:
    risky_operation()
except Exception as error:
    print(error)
```

Even better, when you know the exact exception:

```python
try:
    number = 10 / 0
except ZeroDivisionError as error:
    print(error)
```

---

# 4. Python Exception Types

Python has many built-in exceptions.

Some important ones:

| Python              | Meaning                       | JS equivalent                              |
| ------------------- | ----------------------------- | ------------------------------------------ |
| `ValueError`        | Wrong value                   | `TypeError`/custom error depending on case |
| `TypeError`         | Wrong type/operation          | `TypeError`                                |
| `KeyError`          | Dictionary key missing        | Usually `undefined` in JS object access    |
| `IndexError`        | List index doesn't exist      | Usually `undefined`                        |
| `ZeroDivisionError` | Division by zero              | `Error`                                    |
| `FileNotFoundError` | File doesn't exist            | File-system error                          |
| `AttributeError`    | Object doesn't have attribute | `TypeError` often                          |
| `NameError`         | Variable doesn't exist        | `ReferenceError`                           |
| `ImportError`       | Import problem                | Module/import error                        |

---

# 5. `ValueError`

This happens when the **type is valid but the value is invalid**.

Example:

```python
age = int("abc")
```

Python cannot convert `"abc"` to an integer.

You'll get:

```text
ValueError
```

Handle it:

```python
try:
    age = int("abc")
except ValueError:
    print("Invalid age")
```

Output:

```text
Invalid age
```

---

# 6. `TypeError`

Example:

```python
name = "Gowtam"

result = name + 10
```

Python:

```text
TypeError
```

Handle it:

```python
try:
    result = name + 10
except TypeError:
    print("Invalid operation")
```

---

# 7. `ZeroDivisionError`

```python
try:
    result = 100 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Output:

```text
Cannot divide by zero
```

---

# 8. `KeyError` ⭐

Very important when working with dictionaries.

```python
user = {
    "name": "Gowtam",
    "age": 30
}

print(user["email"])
```

Because `"email"` doesn't exist:

```text
KeyError: 'email'
```

Handle it:

```python
try:
    print(user["email"])
except KeyError:
    print("Email not found")
```

But remember what you learned earlier:

```python
user.get("email")
```

is often better when the key is optional.

---

# 9. `IndexError`

For lists:

```python
numbers = [10, 20, 30]

print(numbers[10])
```

This causes:

```text
IndexError
```

Handle:

```python
try:
    print(numbers[10])
except IndexError:
    print("Index doesn't exist")
```

---

# 10. Multiple `except`

You can handle different errors differently.

```python
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Number cannot be zero")
```

This is similar to checking different error classes in JavaScript.

---

# 11. Multiple Exceptions Together

If you want the same handling:

```python
try:
    risky_operation()

except (ValueError, TypeError):
    print("Invalid input")
```

You can catch multiple exception types.

---

# 12. `else` ⭐

Python has something JavaScript developers may find interesting.

You can use:

```python
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Division failed")

else:
    print("Division successful")
```

Output:

```text
Division successful
```

### What does `else` mean?

`else` runs **only when no exception occurs**.

Think:

```text
try
 ↓
Error?
 ├── YES → except
 └── NO  → else
              ↓
           finally
```

---

# 13. `finally`

`finally` always runs.

```python
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Error")

finally:
    print("Finished")
```

Output:

```text
Finished
```

Even if an exception happens:

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Error")

finally:
    print("Finished")
```

Output:

```text
Error
Finished
```

---

# 14. JavaScript Comparison

### JavaScript

```javascript
try {
  const result = riskyOperation();
} catch (error) {
  console.log("Something went wrong");
} finally {
  console.log("Finished");
}
```

### Python

```python
try:
    result = risky_operation()

except Exception as error:
    print("Something went wrong")

finally:
    print("Finished")
```

---

# 15. `raise` → `throw`

This is extremely important.

JavaScript:

```javascript
throw new Error("User not found");
```

Python:

```python
raise Exception("User not found")
```

So:

```text
JavaScript:
throw

Python:
raise
```

---

# 16. Raising a Specific Exception

Instead of generic `Exception`:

```python
raise ValueError("Invalid amount")
```

Example:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    return age
```

Then:

```python
try:
    set_age(-10)

except ValueError as error:
    print(error)
```

Output:

```text
Age cannot be negative
```

---

# 17. Custom Exceptions ⭐⭐

You can create your own exception class.

```python
class ExpenseNotFoundError(Exception):
    pass
```

Then:

```python
raise ExpenseNotFoundError("Expense not found")
```

Handle it:

```python
try:
    raise ExpenseNotFoundError("Expense not found")

except ExpenseNotFoundError as error:
    print(error)
```

This is similar to JavaScript:

```javascript
class ExpenseNotFoundError extends Error {}
```

Then:

```javascript
throw new ExpenseNotFoundError("Expense not found");
```

---

# 18. Real Expense Tracker Example ⭐⭐⭐

Suppose you have:

```python
expenses = [
    {"id": 1, "title": "Lunch", "amount": 250},
    {"id": 2, "title": "Uber", "amount": 380},
]
```

Create a function:

```python
def get_expense(expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            return expense

    raise ValueError("Expense not found")
```

Use it:

```python
try:
    expense = get_expense(10)
    print(expense)

except ValueError as error:
    print(error)
```

Output:

```text
Expense not found
```

---

# 19. Exceptions in FastAPI ⭐⭐⭐

This is directly related to the error you had earlier.

You were using:

```python
raise HTTPException(
    status_code=404,
    detail="Expense not found"
)
```

This is FastAPI's way of returning an HTTP error response.

For example:

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):

    expense = find_expense(expense_id)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return expense
```

If expense doesn't exist, FastAPI returns:

```json
{
  "detail": "Expense not found"
}
```

with HTTP status:

```text
404
```

---

# 20. Important Difference: Python Exception vs FastAPI Exception

This distinction is important.

### Normal Python

```python
raise ValueError("Invalid amount")
```

This is a Python exception.

### FastAPI

```python
raise HTTPException(
    status_code=400,
    detail="Invalid amount"
)
```

This tells FastAPI:

> Return this HTTP error response to the client.

For API development, you'll use `HTTPException` frequently.

---

# 21. Catching and Re-raising

You can catch an error and then raise another error.

```python
def get_expense(expense_id):

    try:
        expense = database_lookup(expense_id)

    except Exception as error:
        print(error)
        raise
```

Notice:

```python
raise
```

without an exception.

This means:

> Re-raise the current exception.

Similar to:

```javascript
catch (error) {
    console.log(error);
    throw error;
}
```

---

# 22. `as error`

When you write:

```python
except Exception as error:
    print(error)
```

`error` contains the exception object.

You can inspect it:

```python
except Exception as error:
    print(type(error))
    print(str(error))
```

Example:

```text
<class 'ValueError'>
invalid literal for int()
```

JavaScript equivalent:

```javascript
catch (error) {
    console.log(error.name);
    console.log(error.message);
}
```

---

# 23. Don't Hide Errors ⚠️

Avoid:

```python
try:
    do_something()
except:
    pass
```

This is dangerous.

Why?

Because the error disappears silently.

Bad:

```python
try:
    save_expense()
except:
    pass
```

You may think the expense was saved when actually it failed.

Better:

```python
try:
    save_expense()

except Exception as error:
    print(f"Failed to save expense: {error}")
    raise
```

Or, in FastAPI, translate it into an appropriate HTTP error.

---

# 24. Exception Handling Flow

Understand this flow:

```python
try:
    print("A")
    x = 10 / 0
    print("B")

except ZeroDivisionError:
    print("C")

else:
    print("D")

finally:
    print("E")
```

Output:

```text
A
C
E
```

Why?

```text
try
 ↓
A
 ↓
10 / 0
 ↓
Exception!
 ↓
except
 ↓
C
 ↓
finally
 ↓
E
```

`B` never executes.

`else` doesn't execute because an exception occurred.

---

# 25. Another Example

```python
try:
    print("A")
    x = 10 / 2
    print("B")

except ZeroDivisionError:
    print("C")

else:
    print("D")

finally:
    print("E")
```

Output:

```text
A
B
D
E
```

Because there was no exception.

---

# 26. Function + Exception

This pattern is very common:

```python
def divide(a, b):

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b
```

Then:

```python
try:
    result = divide(10, 0)

except ValueError as error:
    print(error)
```

This gives you a clean separation:

```text
Function
   ↓
detects problem
   ↓
raise exception
   ↓
caller handles exception
```

---

# 27. Validation Example

For an Expense Tracker:

```python
def create_expense(title, amount):

    if not title:
        raise ValueError("Title is required")

    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    return {
        "title": title,
        "amount": amount
    }
```

Then:

```python
try:
    expense = create_expense(
        "Lunch",
        -500
    )

except ValueError as error:
    print(error)
```

Output:

```text
Amount must be greater than 0
```

---

# 28. Python `assert`

You'll also see:

```python
assert age >= 18
```

If false, Python raises:

```text
AssertionError
```

Example:

```python
age = 15

assert age >= 18
```

This produces:

```text
AssertionError
```

But **don't use `assert` for normal user/API validation**.

For FastAPI request validation, use Pydantic models and explicit validation instead.

---

# 29. Exception Hierarchy ⭐

Python exceptions have a hierarchy.

Conceptually:

```text
BaseException
    │
    └── Exception
          │
          ├── ValueError
          ├── TypeError
          ├── KeyError
          ├── IndexError
          ├── ZeroDivisionError
          └── ...
```

Therefore:

```python
except Exception:
```

can catch many normal application errors.

But:

```python
except ValueError:
```

only catches `ValueError` and its subclasses.

---

# 30. Order of `except` Matters ⚠️

Bad:

```python
try:
    ...
except Exception:
    ...
except ValueError:
    ...
```

The `ValueError` handler will never be reached because `Exception` catches it first.

Correct:

```python
try:
    ...

except ValueError:
    ...

except Exception:
    ...
```

Think of it as:

```text
specific errors
      ↓
general errors
```

---

# 🧠 JavaScript → Python Cheat Sheet

```text
JavaScript                         Python

try { }                            try:

catch (error) { }                 except Exception as error:

finally { }                        finally:

throw new Error("...")             raise Exception("...")

class X extends Error {}            class X(Exception):
                                        pass

error.message                      str(error)

error.name                         type(error)

throw error                        raise
```

---

# 🎯 What You Should Remember

For your Python/FastAPI learning, focus on these first:

### 1. Handle errors

```python
try:
    risky_code()

except Exception as error:
    print(error)
```

### 2. Specific errors

```python
try:
    age = int(value)

except ValueError:
    print("Invalid number")
```

### 3. Raise errors

```python
if amount <= 0:
    raise ValueError("Amount must be positive")
```

### 4. FastAPI errors

```python
raise HTTPException(
    status_code=404,
    detail="Expense not found"
)
```

### 5. Cleanup

```python
try:
    ...
finally:
    ...
```

### 6. Custom exceptions

```python
class ExpenseNotFoundError(Exception):
    pass
```

---

## 🔥 One Final Comparison

### JavaScript

```javascript
function getExpense(id) {
  const expense = expenses.find((e) => e.id === id);

  if (!expense) {
    throw new Error("Expense not found");
  }

  return expense;
}

try {
  const expense = getExpense(10);
  console.log(expense);
} catch (error) {
  console.log(error.message);
}
```

### Python

```python
def get_expense(expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            return expense

    raise ValueError("Expense not found")


try:
    expense = get_expense(10)
    print(expense)

except ValueError as error:
    print(error)
```

The **mental model is almost exactly the same**. The main things to get used to are Python's `except`, `raise`, and the fact that FastAPI uses `HTTPException` to turn application errors into HTTP responses.
