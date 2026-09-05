# 📘 Python Lists — Chapter 7

# List Operators & Membership Operators

We’ll continue exactly in your preferred format: **Part 1 → Part 2 → Part 3**. 

---

# 🟢 PART 1 — IMPORTANT QUESTIONS & ANSWERS

### Q1. What are List Operators?

**Answer:**
**List operators are operators used to perform operations on lists.**

---

### Q2. What does the `+` operator do with lists?

**Answer:**
**The `+` operator joins two or more lists and creates a new list.**

---

### Q3. What is List Concatenation?

**Answer:**
**List concatenation means joining two or more lists together using `+`.**

---

### Q4. What is the `in` operator?

**Answer:**
**`in` checks whether an element exists in a list.**

It returns:

```text
True / False
```

---

### Q5. What is the `not in` operator?

**Answer:**
**`not in` checks whether an element does not exist in a list.**

It also returns:

```text
True / False
```

---

### Q6. What is the difference between `in` and `not in`?

**Answer:**

**`in` → checks whether an element exists.**

**`not in` → checks whether an element does not exist.**

---

### Q7. Does `+` modify the original lists?

**Answer:**
**No. `+` creates a new combined list.**

---

# 💻 PART 2 — QUESTIONS + ANSWERS + BASIC CODE

## Q1. How do you concatenate two lists?

### Answer

**Use the `+` operator to join two lists.**

### Basic Code

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)
```

### Output

```text
[1, 2, 3, 4, 5, 6]
```

### Simple Explanation

```text
list1
  ↓
[1, 2, 3]

      +

list2
  ↓
[4, 5, 6]

      ↓

[1, 2, 3, 4, 5, 6]
```

---

# Q2. Does `+` change the original lists?

### Answer

**No. The `+` operator creates a new list.**

### Basic Code

```python
list1 = [1, 2]
list2 = [3, 4]

result = list1 + list2

print(list1)
print(list2)
print(result)
```

### Output

```text
[1, 2]
[3, 4]
[1, 2, 3, 4]
```

### Simple Explanation

```text
list1 + list2
     ↓
New List
```

The original lists remain unchanged.

---

# Q3. How do you check whether an element exists in a list?

### Answer

**Use the `in` membership operator.**

### Basic Code

```python
numbers = [10, 20, 30, 40]

print(40 in numbers)
```

### Output

```text
True
```

### Simple Explanation

Python checks:

```text
Is 40 present in numbers?
          ↓
         YES
          ↓
        True
```

---

# Q4. How do you check whether an element does not exist?

### Answer

**Use the `not in` membership operator.**

### Basic Code

```python
numbers = [10, 20, 30, 40]

print(50 not in numbers)
```

### Output

```text
True
```

### Simple Explanation

```text
Is 50 NOT present?
       ↓
      YES
       ↓
     True
```

---

# Q5. How do you use both `in` and `not in`?

### Answer

**Use `in` for presence and `not in` for absence.**

### Basic Code

```python
names = ["Ramesh", "Rahul", "Anjali"]

print("Ramesh" in names)
print("Kiran" not in names)
```

### Output

```text
True
True
```

### Simple Explanation

```text
"Ramesh" exists
      ↓
    True

"Kiran" does not exist
      ↓
    True
```

---

# Q6. How do you combine two lists and then search an element?

### Answer

**First concatenate the lists, then use `in` or `not in`.**

### Basic Code

```python
students1 = ["Ramesh", "Rahul"]
students2 = ["Anjali", "Sita"]

students = students1 + students2

print(students)

print("Sita" in students)
print("Kiran" not in students)
```

### Output

```text
['Ramesh', 'Rahul', 'Anjali', 'Sita']
True
True
```

### Simple Explanation

```text
students1
    ↓
[Ramesh, Rahul]

students2
    ↓
[Anjali, Sita]

      +

      ↓

[Ramesh, Rahul, Anjali, Sita]
```

Then:

```text
"Sita" in students
       ↓
      True
```

and:

```text
"Kiran" not in students
       ↓
      True
```

---

# 🎨 MEMORY TRICK

```text
+ 
↓
JOIN
↓
New List
```

```text
in
↓
EXISTS?
↓
True / False
```

```text
not in
↓
DOES NOT EXIST?
↓
True / False
```

---

# 📊 `+` vs `in` vs `not in`

| Operator | Purpose        | Result           |
| -------- | -------------- | ---------------- |
| `+`      | Join lists     | New list         |
| `in`     | Check presence | `True` / `False` |
| `not in` | Check absence  | `True` / `False` |

---

# 🎓 INTERVIEW QUESTIONS

### Q1. What is list concatenation?

**Answer:**
**Joining two or more lists using the `+` operator is called list concatenation.**

---

### Q2. What does `in` return?

**Answer:**
**`in` returns `True` if the element exists; otherwise `False`.**

---

### Q3. What does `not in` return?

**Answer:**
**`not in` returns `True` if the element does not exist; otherwise `False`.**

---

### Q4. Does list concatenation modify the original lists?

**Answer:**
**No. It creates a new list.**

---

### Q5. Which operator is used to check membership?

**Answer:**
**`in` and `not in` are membership operators.**

---

# ⭐ MCQs

### Q1. Which operator joins two lists?

A. `-`

B. `+`

C. `*`

D. `/`

✅ **Answer: B — `+`**

---

### Q2. What is the output?

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

A. `True`

B. `False`

C. `20`

D. Error

✅ **Answer: A — `True`**

---

### Q3. What is the output?

```python
numbers = [10, 20, 30]

print(50 not in numbers)
```

A. `True`

B. `False`

C. `50`

D. Error

✅ **Answer: A — `True`**

---

### Q4. What does list concatenation create?

A. Dictionary

B. Tuple

C. New List

D. Set

✅ **Answer: C — New List**

---

# 📝 PRACTICE QUESTIONS

### ⭐ Easy

Create two lists:

```python
fruits1 = ["Apple", "Banana"]
fruits2 = ["Mango", "Orange"]
```

Join them using `+`.

---

### ⭐⭐ Medium

Create a list of numbers and check whether `40` exists using `in`.

---

### ⭐⭐ Medium

Create a list of names and check:

* `"Ramesh"` using `in`
* `"Kiran"` using `not in`

---

### ⭐⭐⭐ Challenge

Create:

```python
students1 = ["Ramesh", "Rahul"]
students2 = ["Anjali", "Sita"]
```

Then:

1. Combine both lists.
2. Check whether `"Sita"` exists.
3. Check whether `"Kiran"` does not exist.

---

# ✅ PRACTICE ANSWERS

### Answer 1

```python
fruits1 = ["Apple", "Banana"]
fruits2 = ["Mango", "Orange"]

print(fruits1 + fruits2)
```

Output:

```text
['Apple', 'Banana', 'Mango', 'Orange']
```

---

### Answer 2

```python
numbers = [10, 20, 30, 40]

print(40 in numbers)
```

Output:

```text
True
```

---

### Answer 3

```python
names = ["Ramesh", "Rahul", "Anjali"]

print("Ramesh" in names)
print("Kiran" not in names)
```

Output:

```text
True
True
```

---

### Answer 4

```python
students1 = ["Ramesh", "Rahul"]
students2 = ["Anjali", "Sita"]

students = students1 + students2

print(students)
print("Sita" in students)
print("Kiran" not in students)
```

Output:

```text
['Ramesh', 'Rahul', 'Anjali', 'Sita']
True
True
```

These examples and outputs follow the uploaded chapter material. 

---

# 🟡 PART 3 — FINAL SUMMARY TABLE

| Topic         | Simple Meaning                  | Important Keyword  |
| ------------- | ------------------------------- | ------------------ |
| List Operator | Performs operation on lists     | Operator           |
| `+`           | Joins lists                     | Concatenation      |
| Concatenation | Combines lists                  | `list1 + list2`    |
| New List      | Result of `+`                   | Original unchanged |
| `in`          | Checks if element exists        | Membership         |
| `not in`      | Checks if element doesn't exist | Membership         |
| `True`        | Condition is satisfied          | Boolean            |
| `False`       | Condition is not satisfied      | Boolean            |

# 🏆 MASTER MEMORY

```text
             LIST OPERATORS
                    │
          ┌─────────┴─────────┐
          │                   │
         +                Membership
          │                   │
       JOIN              ┌────┴────┐
          │              │         │
     New List            in      not in
                         │         │
                       Exists   Not Exists
                         │         │
                      True/False
```

### 🔥 Interview Must Remember

> **`+` → Join two lists**

> **`in` → Check whether an element exists**

> **`not in` → Check whether an element does not exist**

> **`+` creates a new list and does not modify the original lists.** 

---

## 📖 NEXT — Chapter 8

**Looping Through Lists**

Main concepts:

```python
for num in numbers:
    print(num)
```

```python
for index in range(len(numbers)):
    print(index, numbers[index])
```

```python
for index, name in enumerate(names):
    print(index, name)
```

We’ll continue with the same **Q&A → Q&A + Basic Code → Summary Table** format.
