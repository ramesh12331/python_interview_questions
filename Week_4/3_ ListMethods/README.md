Absolutely 👍 Let’s continue with the **same format**.

# 🟢 PART 1 — IMPORTANT QUESTIONS & ANSWERS

## Q1. What is a List in Python?

A **List is an ordered and mutable collection** that can store multiple values in a single variable.

---

## Q2. Why are Lists called mutable?

Because we can **modify, add, or remove elements after creating the list**.

---

## Q3. Does a List allow duplicate values?

**Yes. Lists allow duplicate values.**

```text
[10, 20, 10, 30]
```

---

## Q4. What is List Indexing?

Indexing is used to **access individual elements using their position**.

**Positive indexing starts from `0`.**

---

## Q5. What is List Slicing?

Slicing is used to **extract a portion of a list**.

Syntax:

```text
list[start:stop:step]
```

---

## Q6. Difference between `append()` and `extend()`?

**`append()` adds one object**, whereas **`extend()` adds multiple elements** from an iterable.

---

## Q7. Difference between `remove()` and `pop()`?

**`remove()` removes by value**, whereas **`pop()` removes by index and returns the removed element.**

---

## Q8. Difference between `sort()` and `reverse()`?

**`sort()` arranges elements in order**, while **`reverse()` only reverses the current order.**

---

## Q9. What is `index()`?

`index()` returns the **position of the first occurrence** of a specified value.

---

## Q10. What is `count()`?

`count()` returns the **number of times a value occurs** in a list.

---

## Q11. How do you loop through a List?

We can use a **`for` loop** to access elements one by one.

---

## Q12. What is `enumerate()`?

`enumerate()` is used when we need **both the index and value while looping**.

---

## Q13. What is List Comprehension?

List comprehension is a **short and efficient way to create a new list in a single line**.

---

## Q14. What is the difference between List and Tuple?

| List                      | Tuple         |
| ------------------------- | ------------- |
| **Mutable**               | **Immutable** |
| Uses `[]`                 | Uses `()`     |
| More modification methods | Fewer methods |

---

## Q15. What are common List errors?

Important errors include:

* **`IndexError`** → invalid index
* **`ValueError`** → value not found for operations such as `remove()`
* **`TypeError`** → incorrect data type for an operation

These points are included in the uploaded revision material. 

---

# 🟡 PART 2 — QUESTIONS + ANSWERS + BASIC CODE

## Q1. What is a List?

### Answer

A **List stores multiple values** and is **ordered and mutable**.

### Basic Code

```python
numbers = [10, 20, 30, 40]

print(numbers)
```

### Output

```text
[10, 20, 30, 40]
```

### Simple Explanation

`numbers` is one variable containing multiple values.

---

## Q2. How does Indexing work?

### Answer

**Indexing starts from `0`.**

### Basic Code

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[2])
print(numbers[-1])
```

### Output

```text
10
30
40
```

### Explanation

```text
10 → index 0
20 → index 1
30 → index 2
40 → index 3
```

`-1` means the **last element**.

---

## Q3. How does Slicing work?

### Answer

Slicing extracts a **portion of a list**.

### Basic Code

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[::-1])
```

### Output

```text
[20, 30, 40]
[50, 40, 30, 20, 10]
```

### Explanation

```text
[start : stop : step]
```

The `stop` index is **not included**.

---

## Q4. How does `append()` work?

### Answer

**`append()` adds one element at the end.**

### Basic Code

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

### Output

```text
[10, 20, 30, 40]
```

---

## Q5. How does `extend()` work?

### Answer

**`extend()` adds multiple elements to the list.**

### Basic Code

```python
numbers = [10, 20]

numbers.extend([30, 40])

print(numbers)
```

### Output

```text
[10, 20, 30, 40]
```

---

## Q6. `append()` vs `extend()`

### Basic Code

```python
a = [1, 2]

a.append([3, 4])

print(a)
```

### Output

```text
[1, 2, [3, 4]]
```

With `extend()`:

```python
a = [1, 2]

a.extend([3, 4])

print(a)
```

### Output

```text
[1, 2, 3, 4]
```

### Interview Point

**`append()` → one object**

**`extend()` → multiple elements**

---

## Q7. How does `remove()` work?

### Answer

**`remove()` removes the first matching value.**

### Basic Code

```python
numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)
```

### Output

```text
[10, 30, 20]
```

### Explanation

Only the **first `20`** is removed.

---

## Q8. How does `pop()` work?

### Answer

**`pop()` removes and returns an element.**

### Basic Code

```python
numbers = [10, 20, 30]

value = numbers.pop(1)

print(value)
print(numbers)
```

### Output

```text
20
[10, 30]
```

---

## Q9. How does `index()` work?

### Answer

**`index()` returns the position of the first occurrence.**

### Basic Code

```python
numbers = [10, 20, 30, 20]

print(numbers.index(20))
```

### Output

```text
1
```

---

## Q10. How does `count()` work?

### Answer

**`count()` returns how many times a value occurs.**

### Basic Code

```python
numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))
```

### Output

```text
3
```

---

## Q11. How do you loop through a List?

### Answer

Use a **`for` loop**.

### Basic Code

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

### Output

```text
10
20
30
```

### Explanation

The loop takes **one element at a time**.

---

## Q12. How do you get index and value together?

### Answer

Use **`enumerate()`**.

### Basic Code

```python
names = ["A", "B", "C"]

for index, name in enumerate(names):
    print(index, name)
```

### Output

```text
0 A
1 B
2 C
```

### Interview Point

**`enumerate()` is a simple way to get both index and value.**

---

## Q13. How do you sort a List?

### Answer

Use **`sort()`**.

### Basic Code

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

### Output

```text
[10, 20, 30, 40]
```

Descending:

```python
numbers.sort(reverse=True)

print(numbers)
```

### Output

```text
[40, 30, 20, 10]
```

---

## Q14. How do you reverse a List?

### Answer

Use **`reverse()`**.

### Basic Code

```python
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

### Output

```text
[40, 30, 20, 10]
```

### Important

**`reverse()` does not sort the values. It only reverses their current order.**

---

## Q15. What is List Comprehension?

### Answer

It is a **short way to create a new list**.

### Basic Code

```python
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)
```

### Output

```text
[1, 4, 9, 16, 25]
```

### Explanation

Instead of writing a complete `for` loop, we create the list in one line.

---

# 🔵 PART 3 — FINAL SUMMARY TABLE

| Topic              | Simple Meaning                      | Important Keyword      |
| ------------------ | ----------------------------------- | ---------------------- |
| List               | Multiple values in one variable     | `[]`                   |
| Ordered            | Maintains sequence                  | Order                  |
| Mutable            | Can be changed                      | Modify                 |
| Duplicate          | Same value can occur multiple times | Duplicates             |
| Indexing           | Access element by position          | `list[0]`              |
| Slicing            | Get part of list                    | `[:]`                  |
| `append()`         | Add one element                     | End                    |
| `insert()`         | Add at specific position            | Index                  |
| `extend()`         | Add multiple elements               | Multiple               |
| `remove()`         | Remove by value                     | Value                  |
| `pop()`            | Remove and return element           | Index                  |
| `clear()`          | Remove everything                   | `[]`                   |
| `index()`          | Find position                       | First occurrence       |
| `count()`          | Count occurrences                   | Frequency              |
| `sort()`           | Arrange values                      | Ascending              |
| `reverse()`        | Reverse current order               | Reverse                |
| `for`              | Loop through values                 | Iteration              |
| `range(len())`     | Access index                        | Index                  |
| `enumerate()`      | Index + value                       | Both                   |
| `break`            | Stop loop completely                | Stop                   |
| `continue`         | Skip current iteration              | Skip                   |
| `len()`            | Number of elements                  | Length                 |
| `sum()`            | Total                               | Sum                    |
| `min()`            | Smallest value                      | Minimum                |
| `max()`            | Largest value                       | Maximum                |
| List Comprehension | Create list in short form           | `[expression for ...]` |
| `IndexError`       | Invalid index                       | Index problem          |
| `ValueError`       | Invalid/missing value               | Value problem          |
| `TypeError`        | Wrong data type                     | Type problem           |

The above revision follows the terminology and coverage in your uploaded Lists material. 

### 🏆 MUST REMEMBER

```text
append()  → ONE
extend()  → MANY

remove()  → VALUE
pop()     → INDEX

index()   → POSITION
count()   → FREQUENCY

sort()    → ARRANGE
reverse() → REVERSE

for       → VALUES
enumerate → INDEX + VALUE

List      → MUTABLE
Tuple     → IMMUTABLE
```

**This is the core Python Lists interview revision.**
