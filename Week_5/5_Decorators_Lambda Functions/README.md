# 🎯 Advanced Python Functions — Mock Interview

Based on your uploaded material, I’ve filtered the **important interview questions** and kept the answers short and easy to remember. 

---

# PART 1 — 🎯 Questions & Answers

## 🔹 Generators

### Q1. What is a Generator?

**Answer:** A generator is a special function that uses **`yield` to produce values one at a time**.

### Q2. Which keyword is used in a Generator?

**Answer:** The **`yield` keyword** is used in generators.

### Q3. What does `yield` do?

**Answer:** **`yield` gives one value and pauses the function.** When requested again, the function continues from where it paused.

### Q4. What does `next()` do?

**Answer:** **`next()` retrieves the next value from a generator.**

### Q5. What is the difference between `yield` and `return`?

**Answer:** **`return` finishes the function**, while **`yield` pauses the function and allows it to continue later**.

### Q6. Why are Generators useful?

**Answer:** Generators are useful because they **produce values one at a time and can save memory**, especially when processing large data.

---

## 🔹 `filter()`

### Q7. What is `filter()`?

**Answer:** `filter()` is used to **select elements from an iterable based on a condition**.

### Q8. What is the syntax of `filter()`?

**Answer:** The syntax is **`filter(function, iterable)`**.

### Q9. What does `filter()` return?

**Answer:** `filter()` returns a **filter object**. We can convert it to a list using `list()`.

### Q10. Can we use `filter()` with Lambda?

**Answer:** Yes. **`filter()` is commonly used with `lambda` to apply a condition easily.**

---

## 🔹 First-Class Functions

### Q11. What are First-Class Functions?

**Answer:** In Python, **functions are first-class objects**, meaning they can be treated like other objects.

### Q12. What can we do with First-Class Functions?

**Answer:** A function can be **assigned to a variable, passed to another function, and returned from another function**.

### Q13. Why are First-Class Functions important?

**Answer:** They are important because **they make concepts such as decorators possible**.

---

## 🔹 Decorators

### Q14. What is a Decorator?

**Answer:** A decorator is a function that **adds extra functionality to another function without changing its main code**.

### Q15. What is a Wrapper Function?

**Answer:** A wrapper is an **inner function that wraps and calls the original function**.

### Q16. What does `@decorator` mean?

**Answer:** `@decorator` is syntax used to **apply a decorator to a function**.

### Q17. Why do we use `*args` and `**kwargs` in decorators?

**Answer:** They allow the decorator to **work with functions having different types and numbers of arguments**.

### Q18. What are common uses of Decorators?

**Answer:** Common uses include **timing, logging, authentication, validation, permissions, and reusable before/after logic**.

---

# PART 2 — 💻 Questions + Answers + Basic Code

## 🔹 Generators

### Q1. What is a Generator?

**Answer:** A generator is a special function that uses **`yield` to produce values one at a time**.

### Basic Code

```python
def numbers():
    yield 10
    yield 20
    yield 30


a = numbers()

print(next(a))
print(next(a))
print(next(a))
```

**Output:**

```text
10
20
30
```

👉 **`yield` produces one value at a time.**

---

### Q2. What does `next()` do?

**Answer:** **`next()` retrieves the next value from a generator.**

### Basic Code

```python
def generate():
    yield 1
    yield 2
    yield 3


a = generate()

print(next(a))
print(next(a))
```

**Output:**

```text
1
2
```

👉 Every `next()` asks the generator for the **next available value**.

---

### Q3. What is the difference between `yield` and `return`?

**Answer:** **`return` finishes the function**, while **`yield` pauses the function and allows it to continue later**.

### Basic Code

```python
def test():
    yield 10
    yield 20


a = test()

print(next(a))
print(next(a))
```

**Output:**

```text
10
20
```

👉 The generator **pauses at `yield` and resumes from there**.

---

## 🔹 `filter()`

### Q4. What is `filter()`?

**Answer:** `filter()` is used to **select elements from an iterable based on a condition**.

### Basic Code

```python
numbers = [1, 2, 3, 4, 5, 6]

result = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(result)
```

**Output:**

```text
[2, 4, 6]
```

👉 The condition keeps only the **even numbers**.

---

### Q5. Can we use `filter()` with Lambda?

**Answer:** Yes. **`filter()` and `lambda` can be used together to filter values based on a condition.**

### Basic Code

```python
numbers = [1, 2, 3, 4, 5]

result = list(
    filter(lambda x: x > 3, numbers)
)

print(result)
```

**Output:**

```text
[4, 5]
```

👉 `lambda` checks the condition, and `filter()` keeps the matching values.

---

## 🔹 First-Class Functions

### Q6. What are First-Class Functions?

**Answer:** In Python, **functions are first-class objects**, so they can be assigned, passed, and returned.

### Basic Code

```python
def add(x, y):
    return x + y


a = add

print(a(10, 20))
```

**Output:**

```text
30
```

👉 The function `add` is **assigned to another variable `a`**.

---

### Q7. Can a function return another function?

**Answer:** Yes. **A function can return another function because functions are first-class objects.**

### Basic Code

```python
def fun():

    def add(x, y):
        return x + y

    return add


a = fun()

print(a(10, 20))
```

**Output:**

```text
30
```

👉 `fun()` returns the `add` function.

👉 This concept is the **foundation of decorators**.

---

# 🔹 Decorators

### Q8. What is a Decorator?

**Answer:** A decorator is a function that **adds extra functionality to another function without changing the original function's main code**.

### Basic Code

```python
def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


def greet():
    print("Hello")


greet = decorator(greet)

greet()
```

**Output:**

```text
Before
Hello
After
```

👉 The decorator adds **extra behavior before and after** `greet()`.

---

### Q9. What is a Wrapper Function?

**Answer:** A wrapper is an **inner function that wraps and calls the original function**.

### Basic Code

```python
def decorator(func):

    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


@decorator
def greet():
    print("Hello")


greet()
```

**Output:**

```text
Start
Hello
End
```

👉 `wrapper()` surrounds the original `greet()` function.

---

### Q10. What does `@decorator` mean?

**Answer:** `@decorator` is syntax used to **apply a decorator to a function**.

### Basic Code

```python
def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@decorator
def greet():
    print("Hello")


greet()
```

👉

```python
@decorator
```

is essentially equivalent to:

```python
greet = decorator(greet)
```

**⭐ This is a very important interview point.**

---

### Q11. Why do we use `*args` and `**kwargs` in decorators?

**Answer:** They allow the decorator to **work with functions having different arguments**.

### Basic Code

```python
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(10, 20))
```

**Output:**

```text
Before
After
30
```

👉 `*args` handles **positional arguments**.

👉 `**kwargs` handles **keyword arguments**.

---

### Q12. What is a Timer Decorator?

**Answer:** A timer decorator is used to **measure how much time a function takes to execute**.

### Basic Code

```python
import time


def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Time:", end - start)

        return result

    return wrapper


@timer
def add(a, b):
    return a + b


print(add(10, 20))
```

👉 The decorator executes the function and **calculates the execution time**.

---

# 📊 PART 3 — FINAL SUMMARY TABLE

| Topic                           | Simple Meaning                             | Important Keyword / Concept |
| ------------------------------- | ------------------------------------------ | --------------------------- |
| **Generator**                   | Produces values one at a time              | `yield`                     |
| **`yield`**                     | Pauses and resumes function                | `yield`                     |
| **`next()`**                    | Gets the next generator value              | `next()`                    |
| **Generator Advantage**         | Saves memory for sequential processing     | One value at a time         |
| **`filter()`**                  | Selects values based on a condition        | `filter()`                  |
| **Lambda + filter**             | Filters using a short condition            | `lambda`                    |
| **First-Class Function**        | Function can be assigned, passed, returned | Function object             |
| **Function Returning Function** | One function returns another function      | `return add`                |
| **Decorator**                   | Adds extra functionality to a function     | `@decorator`                |
| **Wrapper**                     | Wraps the original function                | `wrapper()`                 |
| **`*args`**                     | Handles positional arguments               | `*args`                     |
| **`**kwargs`**                  | Handles keyword arguments                  | `**kwargs`                  |
| **Timer Decorator**             | Measures function execution time           | `time.time()`               |

### ⭐ Final Interview Connection

**First-Class Functions → Function Returning Function → Wrapper → Decorator → `@decorator` → `*args / **kwargs`**

This is the **most important connection** to understand for decorators. 
