# 🐍 Python Sets — Part 1: Important Interview Questions & Answers

Based on your **Python Sets – Final Revision & Interview Summary**. 

## 1. What is a Set in Python?

**Answer:**
A **Set is an unordered collection of unique elements**.

The main advantage is that **duplicate values are automatically removed**.

---

## 2. What are the characteristics of a Set?

**Answer:**

A Set is:

* **Unordered**
* **Mutable**
* **Does not allow duplicates**
* **Does not support indexing**
* **Does not support slicing**
* Provides **fast membership testing**

---

## 3. Are Sets ordered?

**Answer:**
**No. Sets are unordered collections.**

Therefore, we should not depend on the position/order of elements.

---

## 4. Are Sets mutable?

**Answer:**
**Yes. Sets are mutable.**

We can add or remove elements after creating a Set.

---

## 5. Does a Set allow duplicate values?

**Answer:**
**No. Sets store only unique values.**

Duplicate values are automatically removed.

---

## 6. Can we access Set elements using indexing?

**Answer:**
**No. Sets do not support indexing.**

For example, `s[0]` is invalid.

We can use a **`for` loop** to access elements.

---

## 7. How do you create an empty Set?

**Answer:**
Use **`set()`**.

Important:

**`{}` creates an empty Dictionary, not an empty Set.**

---

## 8. What is the difference between `add()` and `update()`?

**Answer:**

* **`add()` → adds one element**
* **`update()` → adds multiple elements**

This is an important interview question.

---

## 9. What is the difference between `remove()` and `discard()`?

**Answer:**

* **`remove()` → removes an element and raises `KeyError` if it doesn't exist**
* **`discard()` → removes an element safely and does not raise an error if it doesn't exist**

---

## 10. What does `pop()` do in a Set?

**Answer:**
`pop()` **removes and returns one arbitrary element**.

Because Sets are unordered, we should not expect a particular element to be removed.

---

## 11. What does `clear()` do?

**Answer:**
`clear()` **removes all elements from the Set**, leaving an empty Set.

---

## 12. What does `copy()` do?

**Answer:**
`copy()` **creates another Set containing the same elements**.

---

## 13. What is Union?

**Answer:**
**Union returns all unique elements from both Sets.**

Operator: **`|`**

---

## 14. What is Intersection?

**Answer:**
**Intersection returns the common elements between two Sets.**

Operator: **`&`**

---

## 15. What is Difference?

**Answer:**
**Difference returns elements that are present in the first Set but not in the second Set.**

Operator: **`-`**

---

## 16. What is Symmetric Difference?

**Answer:**
**Symmetric Difference returns elements that are in either Set but not in both.**

Operator: **`^`**

---

## 17. What is a Subset?

**Answer:**
A Set is a **subset** when all its elements are present inside another Set.

Method: **`issubset()`**

---

## 18. What is a Superset?

**Answer:**
A Set is a **superset** when it contains all elements of another Set.

Method: **`issuperset()`**

---

## 19. What is Set Comprehension?

**Answer:**
**Set Comprehension is a concise way to create a Set using an expression and iterable.**

Basic syntax:

```python
{expression for variable in iterable}
```

---

## 20. Why are Sets fast for searching?

**Answer:**
Sets use **hash tables**, which provide **average O(1) membership testing**.

So checking whether an element exists using `in` is generally very fast.

---

## 21. Why can't we modify a Set while iterating?

**Answer:**
Modifying a Set while iterating can cause a **`RuntimeError`**.

If modification is required, we can iterate over a **copy of the Set**.

---

# 🧑‍💻 Part 2 — Questions + Answers + Basic Code

## 1. How do you create a Set?

**Answer:**
Use curly braces `{}` with elements.

### Basic Code

```python
numbers = {10, 20, 30}

print(numbers)
print(type(numbers))
```

### Output

```text
{10, 20, 30}
<class 'set'>
```

### Simple Explanation

`{10, 20, 30}` creates a Set containing three unique elements.

---

## 2. How do you create an empty Set?

**Answer:**
Use **`set()`**.

### Basic Code

```python
s = set()

print(s)
print(type(s))
```

### Output

```text
set()
<class 'set'>
```

### Important

```python
s = {}
```

creates a **Dictionary**, not a Set.

---

## 3. How does a Set remove duplicates?

**Answer:**
A Set automatically keeps **only unique values**.

### Basic Code

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

### Output

```text
{10, 20, 30}
```

### Explanation

`10` and `20` appeared more than once, but the Set kept them only once.

---

## 4. How does `add()` work?

**Answer:**
**`add()` adds one element to a Set.**

### Basic Code

```python
s = {10, 20}

s.add(30)

print(s)
```

### Output

```text
{10, 20, 30}
```

---

## 5. How does `update()` work?

**Answer:**
**`update()` adds multiple elements.**

### Basic Code

```python
s = {10, 20}

s.update([30, 40, 50])

print(s)
```

### Output

```text
{10, 20, 30, 40, 50}
```

---

## 6. What is the difference between `add()` and `update()`?

### Basic Code

```python
s = {10, 20}

s.add(30)

print(s)

s.update([40, 50])

print(s)
```

### Output

```text
{10, 20, 30}
{10, 20, 30, 40, 50}
```

### Remember

**`add()` → one element**
**`update()` → multiple elements**

---

## 7. How does `remove()` work?

**Answer:**
`remove()` removes an element. If the element is missing, it raises **`KeyError`**.

### Basic Code

```python
s = {10, 20, 30}

s.remove(20)

print(s)
```

### Output

```text
{10, 30}
```

---

## 8. How does `discard()` work?

**Answer:**
`discard()` safely removes an element.

### Basic Code

```python
s = {10, 20, 30}

s.discard(100)

print(s)
```

### Output

```text
{10, 20, 30}
```

### Important

**`discard()` does not raise an error when the element is missing.**

---

## 9. What is the difference between `remove()` and `discard()`?

```python
s = {10, 20, 30}

s.remove(20)
print(s)

s.discard(100)
print(s)
```

### Output

```text
{10, 30}
{10, 30}
```

**Interview shortcut:**

> **`remove()` = error if missing**
> **`discard()` = safe if missing**

---

## 10. How does `pop()` work?

**Answer:**
`pop()` removes and returns **one arbitrary element**.

### Basic Code

```python
s = {10, 20, 30}

value = s.pop()

print("Removed:", value)
print("Set:", s)
```

### Output

The removed element can vary because **Sets are unordered**.

---

## 11. How does `clear()` work?

### Basic Code

```python
s = {10, 20, 30}

s.clear()

print(s)
```

### Output

```text
set()
```

**`clear()` → removes everything.**

---

## 12. How do you access elements of a Set?

**Answer:**
Sets don't support indexing, so use a **loop**.

### Basic Code

```python
s = {10, 20, 30}

for item in s:
    print(item)
```

### Output

```text
10
20
30
```

The order may vary because **Sets are unordered**.

---

## 13. How do you check whether an element exists?

**Answer:**
Use the **`in` membership operator**.

### Basic Code

```python
s = {10, 20, 30}

print(20 in s)
print(50 in s)
```

### Output

```text
True
False
```

---

# 🔥 Set Operators

Assume:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

## 14. What is Union?

### Basic Code

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)
```

### Output

```text
{1, 2, 3, 4, 5, 6}
```

**Union = everything, without duplicates.**

---

## 15. What is Intersection?

### Basic Code

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A & B)
```

### Output

```text
{3, 4}
```

**Intersection = common elements.**

---

## 16. What is Difference?

### Basic Code

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A - B)
```

### Output

```text
{1, 2}
```

**Difference = first Set only.**

---

## 17. What is Symmetric Difference?

### Basic Code

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A ^ B)
```

### Output

```text
{1, 2, 5, 6}
```

**Symmetric Difference = everything except common elements.**

---

# 🔥 Subset & Superset

## 18. What is `issubset()`?

### Basic Code

```python
A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))
```

### Output

```text
True
```

**A is inside B → A is a subset of B.**

---

## 19. What is `issuperset()`?

### Basic Code

```python
A = {1, 2}
B = {1, 2, 3}

print(B.issuperset(A))
```

### Output

```text
True
```

**B contains A → B is a superset of A.**

---

# 🔥 Set Comprehension

## 20. What is Set Comprehension?

### Basic Code

```python
numbers = {x * x for x in range(1, 6)}

print(numbers)
```

### Output

```text
{1, 4, 9, 16, 25}
```

### With Condition

```python
even = {x for x in range(1, 11) if x % 2 == 0}

print(even)
```

### Output

```text
{2, 4, 6, 8, 10}
```

**Set Comprehension = short way to create Sets.**

---

# ⚠️ Important Common Errors

## Error 1 — `{}` for Empty Set

```python
s = {}
print(type(s))
```

Output:

```text
<class 'dict'>
```

Correct:

```python
s = set()
```

---

## Error 2 — Indexing

```python
s = {10, 20, 30}

print(s[0])
```

This causes:

```text
TypeError
```

**Sets do not support indexing.**

---

## Error 3 — `remove()` with Missing Element

```python
s = {10, 20, 30}

s.remove(100)
```

This causes:

```text
KeyError
```

Use:

```python
s.discard(100)
```

when you want safe removal.

---

# 🏆 Part 3 — Final Summary Table

| Topic                | Simple Meaning               | Important Keyword / Concept |
| -------------------- | ---------------------------- | --------------------------- |
| Set                  | Collection of unique values  | `set`                       |
| Order                | No fixed order               | **Unordered**               |
| Mutable              | Can change Set               | **Mutable**                 |
| Duplicates           | Not allowed                  | **Unique values**           |
| Empty Set            | Creates empty Set            | `set()`                     |
| `{}`                 | Creates Dictionary           | **Not Set**                 |
| Add one              | Add one element              | `add()`                     |
| Add many             | Add multiple elements        | `update()`                  |
| Remove               | Error if missing             | `remove()`                  |
| Safe remove          | No error if missing          | `discard()`                 |
| Remove one           | Removes arbitrary element    | `pop()`                     |
| Remove all           | Empty the Set                | `clear()`                   |
| Copy                 | Creates another Set          | `copy()`                    |
| Access               | Use loop                     | `for`                       |
| Search               | Check membership             | `in`                        |
| Union                | All unique elements          | `\|`                        |
| Intersection         | Common elements              | `&`                         |
| Difference           | First Set only               | `-`                         |
| Symmetric Difference | Non-common elements          | `^`                         |
| Subset               | Small Set inside another     | `issubset()`                |
| Superset             | Large Set containing another | `issuperset()`              |
| Set Comprehension    | Short Set creation           | `{x for x in ...}`          |
| Search Complexity    | Fast membership test         | **Average O(1)**            |
| Hash Table           | Reason for fast lookup       | **Hashing**                 |
| Set during iteration | Don't directly modify        | `RuntimeError`              |
| Safe iteration       | Iterate over copy            | `s.copy()`                  |

## 🧠 Must Remember for Interview

**Set → Unique Values → Unordered → Mutable → No Indexing**

**`{}` → Dictionary ❌**
**`set()` → Empty Set ✅**

**`add()` → One**
**`update()` → Many**

**`remove()` → Error if missing**
**`discard()` → Safe**

**`pop()` → One arbitrary element**
**`clear()` → Everything**

**`|` → Union → Everything**
**`&` → Intersection → Common**
**`-` → Difference → First only**
**`^` → Symmetric Difference → Non-common**

### ⭐ Golden Interview Answer

> **I use a Set when I need unique values and fast membership testing. Sets automatically remove duplicates and provide average O(1) lookup time.** 
