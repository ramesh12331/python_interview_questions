# 📘 Python Exception Handling — Mock Interview

I’ll continue with your exact format:

**Part 1 → Questions & Answers**
**Part 2 → Questions + Answers + Basic Code + Output + Explanation**
**Part 3 → Final Summary Table**

I’ve filtered the material to the **most important mock-interview questions**. 

---

# 🎯 PART 1 — Important Questions & Answers

## 🔹 Exception Handling

### Q1. What is an Error?

**Answer:** An error is a problem in a program that **prevents the program from executing correctly**.

### Q2. What is an Exception?

**Answer:** An exception is a runtime problem that **interrupts the normal flow of program execution**.

### Q3. What is the difference between SyntaxError and Exception?

**Answer:** **SyntaxError occurs when Python grammar is incorrect**, while exceptions generally occur during program execution.

### Q4. What is `try`?

**Answer:** `try` contains the **code that may cause an exception**.

### Q5. What is `except`?

**Answer:** `except` is used to **handle an exception**.

### Q6. Can we use multiple `except` blocks?

**Answer:** Yes. **Multiple `except` blocks can handle different types of exceptions**.

### Q7. What is `Exception as e`?

**Answer:** `e` refers to the **exception object that was caught**.

### Q8. What is `else` in exception handling?

**Answer:** `else` executes **only when the `try` block completes without an exception**.

### Q9. What is `finally`?

**Answer:** `finally` executes **whether an exception occurs or not** and is commonly used for cleanup.

### Q10. What is `raise`?

**Answer:** `raise` is used to **manually generate or signal an exception**.

---

# 🔹 Custom Exceptions

### Q11. What is a Custom Exception?

**Answer:** A custom exception is a **programmer-defined exception used for application-specific errors**.

### Q12. How do you create a Custom Exception?

**Answer:** We normally create it by **inheriting from the `Exception` class**.

### Q13. Which OOP concept is used in Custom Exceptions?

**Answer:** **Inheritance** is used to create custom exceptions.

### Q14. What is `super()` used for in a Custom Exception?

**Answer:** `super()` is used to **access parent-class functionality**, such as initializing the exception message.

### Q15. What is the difference between `raise` and `except`?

**Answer:** **`raise` signals an exception, while `except` handles an exception**.

### Q16. Can a Custom Exception have methods?

**Answer:** Yes. **A custom exception is a class, so it can contain methods and other class behavior**.

---

# 💻 PART 2 — Questions + Answers + Basic Code

## 🔹 1. What is an Exception?

**Answer:** An exception is a runtime problem that **interrupts the normal flow of a program**.

### Basic Code

```python
print("Start")

print(10 / 0)

print("End")
```

**Output:**

```text
Start
ZeroDivisionError
```

👉 The program stops when `10 / 0` causes an exception.

---

## 🔹 2. What is `try-except`?

**Answer:** `try-except` is used to **handle runtime exceptions in a controlled way**.

### Basic Code

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

**Output:**

```text
Cannot divide by zero
```

👉 `try` contains risky code, and `except` handles the error.

---

## 🔹 3. What is `IndexError`?

**Answer:** `IndexError` occurs when we **access an index that does not exist**.

### Basic Code

```python
numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Invalid index")
```

**Output:**

```text
Invalid index
```

👉 Valid indexes are `0`, `1`, and `2`.

---

## 🔹 4. What is `KeyError`?

**Answer:** `KeyError` occurs when a **dictionary key does not exist**.

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 30
}

try:
    print(student["salary"])

except KeyError:
    print("Key not found")
```

**Output:**

```text
Key not found
```

---

## 🔹 5. What is `TypeError`?

**Answer:** `TypeError` occurs when an operation is **not supported between the given data types**.

### Basic Code

```python
try:
    print(10 + "20")

except TypeError:
    print("Invalid data types")
```

**Output:**

```text
Invalid data types
```

---

## 🔹 6. What is `ValueError`?

**Answer:** `ValueError` occurs when the **data type is correct but the value is invalid**.

### Basic Code

```python
try:
    age = int("twenty")

except ValueError:
    print("Invalid value")
```

**Output:**

```text
Invalid value
```

---

## 🔹 7. What is `Exception as e`?

**Answer:** `e` represents the **caught exception object**.

### Basic Code

```python
try:
    print(10 / 0)

except Exception as e:
    print(e)
```

**Output:**

```text
division by zero
```

👉 `e` stores the exception object.

---

## 🔹 8. What is `else`?

**Answer:** `else` executes **when no exception occurs in the `try` block**.

### Basic Code

```python
try:
    age = int("25")

except ValueError:
    print("Invalid age")

else:
    print("Age:", age)
```

**Output:**

```text
Age: 25
```

👉 Exception → `except`
👉 No exception → `else`

---

## 🔹 9. What is `finally`?

**Answer:** `finally` **executes whether an exception occurs or not**.

### Basic Code

```python
try:
    print("Try")

except:
    print("Except")

finally:
    print("Finally")
```

**Output:**

```text
Try
Finally
```

👉 `finally` is commonly used for **cleanup operations**.

---

## 🔹 10. What is `raise`?

**Answer:** `raise` is used to **manually signal an exception**.

### Basic Code

```python
age = 15

if age < 18:
    raise Exception("Age must be 18 or above")
```

**Output:**

```text
Exception: Age must be 18 or above
```

👉 Python normally detects some errors automatically, but **`raise` allows us to create our own error condition**.

---

# 🔹 11. What is a Custom Exception?

**Answer:** A custom exception is a **programmer-defined exception for a specific application problem**.

### Basic Code

```python
class BankException(Exception):
    pass


raise BankException("Insufficient Balance")
```

**Output:**

```text
BankException: Insufficient Balance
```

👉 `BankException` is our own exception class.

---

# 🔹 12. Which OOP concept is used in Custom Exceptions?

**Answer:** **Inheritance** is used.

### Basic Code

```python
class BankException(Exception):
    pass
```

👉

```text
Exception
    ↓
BankException
```

`BankException` inherits from `Exception`.

---

# 🔹 13. How do you handle a Custom Exception?

**Answer:** We can handle it using **`try-except` with the custom exception class**.

### Basic Code

```python
class BankException(Exception):
    pass


try:
    raise BankException("Insufficient Balance")

except BankException as e:
    print(e)
```

**Output:**

```text
Insufficient Balance
```

---

# 🔹 14. What is `super()` in a Custom Exception?

**Answer:** `super()` is used to **call parent-class functionality**.

### Basic Code

```python
class BankException(Exception):

    def __init__(self, message):
        super().__init__(message)


try:
    raise BankException("Insufficient Balance")

except BankException as e:
    print(e)
```

**Output:**

```text
Insufficient Balance
```

👉 Here:

```python
super().__init__(message)
```

calls the parent `Exception` initialization.

---

# 🔹 15. Can a Custom Exception have methods?

**Answer:** Yes. **A custom exception is a class, so it can contain methods.**

### Basic Code

```python
class SecurityException(Exception):

    def logout(self):
        print("Logout Successfully")


try:
    raise SecurityException("Security Error")

except SecurityException as e:
    print(e)
    e.logout()
```

**Output:**

```text
Security Error
Logout Successfully
```

---

# 🔹 16. Bank Example with Custom Exception ⭐

**Answer:** A custom exception can be used to **represent business-specific errors such as insufficient balance**.

### Basic Code

```python
class BankException(Exception):
    pass


class Bank:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise BankException("Insufficient Balance")

        self.balance -= amount


account = Bank(5000)

try:
    account.withdraw(10000)

except BankException as e:
    print(e)
```

**Output:**

```text
Insufficient Balance
```

👉 Flow:

```text
withdraw()
    ↓
amount > balance
    ↓
raise BankException
    ↓
except BankException
    ↓
print error
```

---

# ⭐ PART 3 — FINAL SUMMARY TABLE

| Topic                 | Simple Meaning                             | Important Keyword |
| --------------------- | ------------------------------------------ | ----------------- |
| **Error**             | Problem in a program                       | Error             |
| **Exception**         | Runtime problem                            | Exception         |
| **SyntaxError**       | Invalid Python grammar                     | Syntax            |
| **IndexError**        | Invalid index                              | `[]`              |
| **KeyError**          | Missing dictionary key                     | Dictionary        |
| **TypeError**         | Invalid operation between types            | Type              |
| **ValueError**        | Invalid value                              | Value             |
| **NameError**         | Name/variable doesn't exist                | Variable          |
| **AttributeError**    | Attribute/method doesn't exist             | Attribute         |
| **ZeroDivisionError** | Division by zero                           | `/ 0`             |
| **try**               | Contains risky code                        | `try`             |
| **except**            | Handles exception                          | `except`          |
| **Multiple except**   | Handles different exceptions               | `except`          |
| **`as e`**            | Stores exception object                    | `e`               |
| **else**              | Runs when no exception occurs              | `else`            |
| **finally**           | Runs regardless of exception               | `finally`         |
| **raise**             | Manually signals exception                 | `raise`           |
| **Custom Exception**  | Application-specific error                 | `class`           |
| **Inheritance**       | Custom exception inherits from `Exception` | `Exception`       |
| **`super()`**         | Calls parent functionality                 | `super()`         |

---

# 🏆 ⭐ Mock Interview Priority

Study in this order:

**1. Exception**
↓
**2. `try-except`**
↓
**3. Common Exceptions**
↓
**4. Multiple `except`**
↓
**5. `Exception as e`**
↓
**6. `else`**
↓
**7. `finally`**
↓
**8. `raise`**
↓
**9. Custom Exception**
↓
**10. Inheritance + `Exception`**
↓
**11. `super()`**
↓
**12. OOP + Custom Exception**

### 🔥 Must-Remember Sentences

* **`try` contains risky code.**
* **`except` handles exceptions.**
* **`else` runs when no exception occurs.**
* **`finally` runs whether an exception occurs or not.**
* **`raise` manually signals an exception.**
* **Custom exceptions are programmer-defined exceptions.**
* **Custom exceptions normally inherit from `Exception`.**
* **`raise` generates/signals; `except` handles.** 
