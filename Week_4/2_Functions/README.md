# 🐍 Python Functions — Interview Revision

I’ll keep the **same format you requested**: **Part 1 → Part 2 → Part 3**. 

# 🟢 PART 1 — IMPORTANT QUESTIONS & ANSWERS

### Q1. What is a Function?

**Answer:**
A **function is a reusable block of code that performs a specific task.**

---

### Q2. Why do we use Functions?

**Answer:**
Functions help to **reduce code duplication, improve readability, make debugging easier, and make code reusable.**

---

### Q3. What is the syntax of a Function?

**Answer:**

```text
def function_name(parameters):
    statements
```

A function is called using:

```text
function_name(arguments)
```

---

### Q4. What is the difference between Function Definition and Function Call?

**Answer:**
**Function definition creates the function, while function call executes the function.**

---

### Q5. What is a Parameter?

**Answer:**
A **parameter is a variable defined inside the function definition.**

---

### Q6. What is an Argument?

**Answer:**
An **argument is the actual value passed to a function during the function call.**

---

### Q7. What is the difference between Parameter and Argument?

**Answer:**

**Parameter → variable in function definition**
**Argument → actual value passed during function call**

---

### Q8. What is `return`?

**Answer:**
**`return` sends a value back to the caller and immediately ends the function.**

---

### Q9. What is the difference between `print()` and `return`?

**Answer:**
**`print()` displays a value, while `return` sends a value back to the caller and stops the function.**

---

### Q10. What are Default Parameters?

**Answer:**
**Default parameters have predefined values that are used when no argument is supplied.**

---

### Q11. What are Keyword Arguments?

**Answer:**
**Keyword arguments are arguments passed using parameter names.**

---

### Q12. What is `*args`?

**Answer:**
**`*args` accepts any number of positional arguments and stores them in a tuple.**

---

### Q13. What is `**kwargs`?

**Answer:**
**`**kwargs` accepts any number of keyword arguments and stores them in a dictionary.**

---

### Q14. What is Recursion?

**Answer:**
**Recursion is when a function calls itself until a base condition is met.**

---

### Q15. What happens if recursion has no base condition?

**Answer:**
**Infinite recursion occurs and Python eventually raises `RecursionError`.**

---

### Q16. What is a Lambda Function?

**Answer:**
A **lambda function is a small anonymous function written in a single line.**

---

### Q17. Can a function return multiple values?

**Answer:**
**Yes. Python can return multiple values separated by commas, which are packed into a tuple.**

---

### Q18. What happens if a function has no `return` statement?

**Answer:**
**It returns `None` by default.**

---

### Q19. What is a Local Variable?

**Answer:**
A **local variable exists inside a function and is available within that function's scope.**

---

### Q20. Can we pass a function as an argument?

**Answer:**
**Yes. Functions are first-class objects in Python, so they can be passed as arguments.**

---

# 💻 PART 2 — QUESTIONS + ANSWERS + BASIC CODE

## Q1. How do you create and call a function?

### Answer

**Use `def` to define a function and use the function name with parentheses to call it.**

### Basic Code

```python
def greet():
    print("Hello World")


greet()
```

### Output

```text
Hello World
```

### Simple Explanation

```text
Define
  ↓
def greet()
  ↓
Call
  ↓
greet()
  ↓
Execute
```

---

# Q2. What are Parameters and Arguments?

### Answer

**Parameters are variables in the function definition.**

**Arguments are actual values passed during the function call.**

### Basic Code

```python
def add(a, b):
    print(a + b)


add(10, 20)
```

### Output

```text
30
```

### Simple Explanation

```text
def add(a, b):
         ↑  ↑
     Parameters


add(10, 20)
     ↑   ↑
   Arguments
```

---

# Q3. How does `return` work?

### Answer

**`return` sends the result back to the caller.**

### Basic Code

```python
def add(a, b):
    return a + b


result = add(10, 20)

print(result)
```

### Output

```text
30
```

### Simple Explanation

```text
add(10,20)
     ↓
return 30
     ↓
result
     ↓
print()
```

---

# Q4. What happens after `return`?

### Answer

**The function stops immediately. Code written after `return` will not execute.**

### Basic Code

```python
def demo():
    return 10

    print("Hello")


print(demo())
```

### Output

```text
10
```

### Important

```text
return
  ↓
Function stops
  ↓
Code after return is skipped
```

---

# Q5. What is the difference between `print()` and `return`?

### Answer

**`print()` displays the result. `return` sends the result back and allows it to be reused.**

### Basic Code

```python
def add(a, b):
    return a + b


result = add(10, 20)

print(result)
```

### Output

```text
30
```

### Simple Explanation

With `return`:

```python
result = add(10, 20)
```

We can store and reuse the returned value.

---

# Q6. What are Default Parameters?

### Answer

**A default parameter has a predefined value.**

### Basic Code

```python
def welcome(name="Ramesh"):
    print(name)


welcome()
welcome("Rahul")
```

### Output

```text
Ramesh
Rahul
```

### Simple Explanation

```text
welcome()
    ↓
No value
    ↓
"Ramesh" is used
```

But:

```text
welcome("Rahul")
       ↓
"Rahul" replaces default value
```

---

# Q7. What are Keyword Arguments?

### Answer

**Keyword arguments pass values using parameter names.**

### Basic Code

```python
def student(id, name, age):
    print(id, name, age)


student(
    age=22,
    id=101,
    name="Ramesh"
)
```

### Output

```text
101 Ramesh 22
```

### Simple Explanation

Here the order doesn't matter because we explicitly specify:

```text
age=22
id=101
name="Ramesh"
```

---

# Q8. What is `*args`?

### Answer

**`*args` allows a function to accept any number of positional arguments. Python stores them as a tuple.**

### Basic Code

```python
def add(*nums):
    print(sum(nums))


add(2, 3, 4)
```

### Output

```text
9
```

### Simple Explanation

Internally:

```text
nums
 ↓
(2, 3, 4)
 ↓
Tuple
```

---

# Q9. What is `**kwargs`?

### Answer

**`**kwargs` allows a function to accept any number of keyword arguments. Python stores them as a dictionary.**

### Basic Code

```python
def student(**details):
    print(details)


student(
    name="Ramesh",
    age=22,
    city="Hyderabad"
)
```

### Output

```text
{'name': 'Ramesh', 'age': 22, 'city': 'Hyderabad'}
```

### Simple Explanation

```text
kwargs
  ↓
Dictionary
  ↓
key : value
```

---

# Q10. What is the difference between `*args` and `**kwargs`?

### Answer

**`*args` → positional arguments → tuple**

**`**kwargs` → keyword arguments → dictionary**

### Basic Code

```python
def demo(*args, **kwargs):
    print(args)
    print(kwargs)


demo(10, 20, name="Ramesh", age=24)
```

### Output

```text
(10, 20)
{'name': 'Ramesh', 'age': 24}
```

### Memory Trick

```text
*args
  ↓
Tuple

**kwargs
  ↓
Dictionary
```

---

# Q11. What is Recursion?

### Answer

**Recursion means a function calls itself. It must have a base condition to stop.**

### Basic Code

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)


countdown(5)
```

### Output

```text
5
4
3
2
1
```

### Simple Explanation

```text
countdown(5)
     ↓
countdown(4)
     ↓
countdown(3)
     ↓
countdown(2)
     ↓
countdown(1)
     ↓
countdown(0)
     ↓
STOP
```

---

# Q12. What happens without a base condition?

### Answer

**The function keeps calling itself and eventually Python raises `RecursionError`.**

### Basic Code

```python
def demo():
    demo()


demo()
```

### Output

```text
RecursionError
```

---

# Q13. What is a Lambda Function?

### Answer

**Lambda is an anonymous one-line function.**

### Basic Code

```python
square = lambda x: x * x

print(square(5))
```

### Output

```text
25
```

### Simple Explanation

Normal function:

```python
def square(x):
    return x * x
```

Lambda:

```python
square = lambda x: x * x
```

**Lambda is useful for short functions.**

---

# Q14. Can a function return multiple values?

### Answer

**Yes. Multiple values can be returned separated by commas. Python packs them into a tuple.**

### Basic Code

```python
def calc():
    return 10, 20


a, b = calc()

print(a)
print(b)
```

### Output

```text
10
20
```

### Simple Explanation

```text
return 10, 20
      ↓
   Tuple
  (10, 20)
      ↓
a, b
```

---

# Q15. What does a function return when there is no `return`?

### Answer

**Python returns `None` by default.**

### Basic Code

```python
def demo():
    print("Hello")


result = demo()

print(result)
```

### Output

```text
Hello
None
```

---

# Q16. Can a function be passed as an argument?

### Answer

**Yes. Functions are first-class objects in Python.**

### Basic Code

```python
def greet():
    return "Hello"


def call(func):
    print(func())


call(greet)
```

### Output

```text
Hello
```

### Simple Explanation

```text
greet
  ↓
passed to call()
  ↓
func
  ↓
func()
  ↓
Hello
```

**Notice:** `call(greet)` passes the function itself, while `func()` calls it.

---

# 📊 PART 3 — FINAL SUMMARY TABLE

| Topic                | Simple Meaning                | Important Keyword / Concept |
| -------------------- | ----------------------------- | --------------------------- |
| Function             | Reusable block of code        | `def`                       |
| Function Definition  | Creates function              | `def function_name()`       |
| Function Call        | Executes function             | `function_name()`           |
| Parameter            | Variable in definition        | `a, b`                      |
| Argument             | Actual value                  | `10, 20`                    |
| Return               | Sends value back              | `return`                    |
| `print()`            | Displays output               | Screen                      |
| Default Parameter    | Predefined value              | `name="Ramesh"`             |
| Keyword Argument     | Pass using parameter name     | `name="Rahul"`              |
| `*args`              | Multiple positional arguments | Tuple                       |
| `**kwargs`           | Multiple keyword arguments    | Dictionary                  |
| Recursion            | Function calls itself         | Base condition              |
| `RecursionError`     | Recursion doesn't stop        | Missing base condition      |
| Lambda               | Anonymous one-line function   | `lambda`                    |
| Multiple Return      | Returns multiple values       | Tuple                       |
| No `return`          | Returns automatically         | `None`                      |
| Local Variable       | Exists inside function        | Local scope                 |
| Global Variable      | Available outside function    | Global scope                |
| First-Class Function | Function can be passed around | Function as object          |

# 🏆 MASTER MEMORY

```text
             🐍 PYTHON FUNCTIONS
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
      Input        Process       Output
        │            │            │
 Parameters      Function       return
 Arguments         Body
        │
 ┌──────┼───────────────┐
 ↓      ↓               ↓
Default Keyword       *args
                     **kwargs
        │
        ├── Recursion
        │
        └── Lambda
```

### 🔥 Most Important Interview Memory

```text
Parameter  → Definition
Argument   → Function Call

print()    → Display
return     → Send value + Stop

*args      → Positional → Tuple
**kwargs   → Keyword    → Dictionary

Recursion  → Function calls itself
Base case  → Stops recursion

Lambda     → Anonymous one-line function

No return  → None
```

### 🎯 Function Execution Flow

```text
DEFINE
  ↓
CALL
  ↓
ARGUMENTS
  ↓
PARAMETERS
  ↓
EXECUTE
  ↓
RETURN (Optional)
  ↓
CONTINUE
```

**Golden interview sentence:**

> **“A Python function is a reusable block of code that performs a specific task. It can accept inputs through parameters, process the data, and optionally return a result. Functions improve code reusability, readability, and maintainability.”** 
