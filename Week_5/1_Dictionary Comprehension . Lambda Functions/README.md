I’ll continue with the uploaded **Python Dictionary** material in your preferred format:

**Part 1 → Questions & Answers**
**Part 2 → Questions + Answers + Basic Code + Output + Explanation**
**Part 3 → Final Summary Table**. 

# 🟢 PART 1 — IMPORTANT QUESTIONS & ANSWERS

### Q1. What is a Dictionary?

**Answer:**
A **Dictionary is a mutable collection of key-value pairs**.

---

### Q2. Are Dictionary keys unique?

**Answer:**
**Yes. Dictionary keys must be unique.** Duplicate keys are not stored separately.

---

### Q3. Can Dictionary values be duplicated?

**Answer:**
**Yes. Duplicate values are allowed.**

---

### Q4. Is Dictionary mutable?

**Answer:**
**Yes. We can add, update, and remove items from a Dictionary.**

---

### Q5. Are Dictionaries ordered?

**Answer:**
**Yes. Dictionaries preserve insertion order in Python 3.7+.**

---

### Q6. Does Dictionary support indexing?

**Answer:**
**No. Dictionaries are accessed using keys, not indexes.**

---

### Q7. What is the difference between `[]` and `get()`?

**Answer:**
`[]` raises **`KeyError`** when the key doesn't exist.

`get()` returns **`None`** by default when the key doesn't exist, so it is safer.

---

### Q8. What are `keys()`, `values()`, and `items()`?

**Answer:**

* `keys()` → **returns dictionary keys**
* `values()` → **returns dictionary values**
* `items()` → **returns key-value pairs**

---

### Q9. What is `pop()`?

**Answer:**
**`pop()` removes an item using its key.**

---

### Q10. What is `popitem()`?

**Answer:**
**`popitem()` removes the last inserted key-value pair.**

---

### Q11. What is `setdefault()`?

**Answer:**
**`setdefault()` adds a key only when that key does not already exist.**

---

### Q12. What is a Nested Dictionary?

**Answer:**
A **Nested Dictionary is a dictionary containing another dictionary as a value.**

---

### Q13. What is Dictionary Comprehension?

**Answer:**
**Dictionary comprehension is a short way of creating a dictionary using an expression and a loop.**

---

### Q14. Can Dictionary Comprehension use `if` and `if-else`?

**Answer:**
**Yes. Dictionary comprehension supports both conditions and conditional expressions.**

---

### Q15. Why are Dictionaries widely used?

**Answer:**
**Dictionaries are useful for key-based data storage and are widely used in JSON, APIs, databases, configuration, and real-world applications.**

---

# 💻 PART 2 — QUESTIONS + ANSWERS + BASIC CODE

## Q1. How do you create a Dictionary?

### Answer

**Use curly braces `{}` with `key: value` pairs.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24,
    "city": "Hyderabad"
}

print(student)
```

### Output

```text
{'name': 'Ramesh', 'age': 24, 'city': 'Hyderabad'}
```

### Simple Explanation

```text
"name" → Key
"Ramesh" → Value
```

---

## Q2. How do you access a Dictionary value?

### Answer

**Use the key inside square brackets `[]`.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24
}

print(student["name"])
```

### Output

```text
Ramesh
```

### Important

If the key doesn't exist:

```python
print(student["salary"])
```

Output:

```text
KeyError
```

---

## Q3. How does `get()` work?

### Answer

**`get()` safely accesses a value without raising `KeyError` for a missing key.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24
}

print(student.get("name"))
print(student.get("salary"))
```

### Output

```text
Ramesh
None
```

### Remember

```text
student["salary"]       → KeyError
student.get("salary")   → None
```

---

## Q4. How do you add a new item?

### Answer

**Assign a value to a new key.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24
}

student["city"] = "Hyderabad"

print(student)
```

### Output

```text
{'name': 'Ramesh', 'age': 24, 'city': 'Hyderabad'}
```

---

## Q5. How do you update an existing value?

### Answer

**Assign a new value to an existing key.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24
}

student["name"] = "Ajay"

print(student)
```

### Output

```text
{'name': 'Ajay', 'age': 24}
```

---

## Q6. How do you remove an item using `pop()`?

### Answer

**`pop(key)` removes the specified key-value pair.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24,
    "city": "Hyderabad"
}

student.pop("age")

print(student)
```

### Output

```text
{'name': 'Ramesh', 'city': 'Hyderabad'}
```

---

## Q7. What is the difference between `pop()` and `popitem()`?

### Answer

**`pop()` removes an item using a specific key.**

**`popitem()` removes the last inserted item.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24,
    "city": "Hyderabad"
}

student.pop("age")
print(student)
```

Output:

```text
{'name': 'Ramesh', 'city': 'Hyderabad'}
```

With `popitem()`:

```python
student = {
    "name": "Ramesh",
    "age": 24,
    "city": "Hyderabad"
}

student.popitem()

print(student)
```

Output:

```text
{'name': 'Ramesh', 'age': 24}
```

---

## Q8. How do you delete a specific Dictionary item using `del`?

### Answer

**Use `del dictionary[key]`.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24
}

del student["age"]

print(student)
```

### Output

```text
{'name': 'Ramesh'}
```

---

## Q9. How do you remove all Dictionary items?

### Answer

**Use `clear()`.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24
}

student.clear()

print(student)
```

### Output

```text
{}
```

---

## Q10. How do you get all keys?

### Answer

**Use `keys()`.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24
}

print(student.keys())
```

### Output

```text
dict_keys(['name', 'age'])
```

---

## Q11. How do you get all values?

### Answer

**Use `values()`.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24
}

print(student.values())
```

### Output

```text
dict_values(['Ramesh', 24])
```

---

## Q12. How do you get both keys and values?

### Answer

**Use `items()`.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24
}

print(student.items())
```

### Output

```text
dict_items([('name', 'Ramesh'), ('age', 24)])
```

---

## Q13. How do you loop through a Dictionary?

### Answer

**`items()` is commonly used when we need both key and value.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24
}

for key, value in student.items():
    print(key, value)
```

### Output

```text
name Ramesh
age 24
```

### Simple Explanation

```text
items()
   ↓
key + value
   ↓
for loop
```

---

## Q14. How do you check whether a key exists?

### Answer

**Use the `in` membership operator.**

### Basic Code

```python
student = {
    "name": "Ramesh",
    "age": 24
}

print("name" in student)
print("salary" in student)
```

### Output

```text
True
False
```

**Important: `in` checks dictionary keys.**

---

## Q15. What does `setdefault()` do?

### Answer

**It adds a key only if the key is missing.**

### Basic Code

```python
student = {
    "name": "Ramesh"
}

student.setdefault("grade", "A")

print(student)
```

### Output

```text
{'name': 'Ramesh', 'grade': 'A'}
```

If `"grade"` already exists, its existing value is not replaced.

---

# 🧩 NESTED & COMBINED STRUCTURES

## Q16. What is a Nested Dictionary?

### Answer

**A Dictionary inside another Dictionary is called a Nested Dictionary.**

### Basic Code

```python
students = {
    101: {
        "name": "Ramesh",
        "marks": 90
    },
    102: {
        "name": "Ajay",
        "marks": 80
    }
}

print(students[101]["marks"])
```

### Output

```text
90
```

### Simple Explanation

```text
students
   ↓
101
   ↓
Dictionary
   ↓
marks
   ↓
90
```

---

## Q17. What is a Dictionary of Lists?

### Answer

**A Dictionary where values are lists is called a Dictionary of Lists.**

### Basic Code

```python
employee = {
    "names": ["A", "B", "C"],
    "salary": [1000, 2000, 3000]
}

print(employee["names"][0])
```

### Output

```text
A
```

---

## Q18. What is a List of Dictionaries?

### Answer

**A List containing dictionaries is called a List of Dictionaries.**

### Basic Code

```python
employees = [
    {"id": 101, "name": "Ramesh"},
    {"id": 102, "name": "Ajay"}
]

print(employees[0]["name"])
```

### Output

```text
Ramesh
```

### Remember

```text
Dictionary of Lists
Dictionary → List

List of Dictionaries
List → Dictionary
```

---

# ⚡ DICTIONARY COMPREHENSION

## Q19. What is Dictionary Comprehension?

### Answer

**It provides a short way to create dictionaries.**

### Basic Code

```python
result = {
    i: i * i
    for i in range(1, 6)
}

print(result)
```

### Output

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Simple Explanation

Normal approach:

```python
result = {}

for i in range(1, 6):
    result[i] = i * i
```

Comprehension:

```python
result = {i: i*i for i in range(1, 6)}
```

**Same result, shorter syntax.**

---

## Q20. Can Dictionary Comprehension use `if`?

### Answer

**Yes.**

### Basic Code

```python
result = {
    i: i
    for i in range(1, 11)
    if i % 2 == 0
}

print(result)
```

### Output

```text
{2: 2, 4: 4, 6: 6, 8: 8, 10: 10}
```

---

## Q21. Can Dictionary Comprehension use `if-else`?

### Answer

**Yes.**

### Basic Code

```python
numbers = {
    i: "Even" if i % 2 == 0 else "Odd"
    for i in range(1, 6)
}

print(numbers)
```

### Output

```text
{
    1: 'Odd',
    2: 'Even',
    3: 'Odd',
    4: 'Even',
    5: 'Odd'
}
```

---

# 🆚 DICTIONARY VS OTHER COLLECTIONS

## Q22. What is the difference between List, Tuple, Set, and Dictionary?

### Answer

| Feature    | List | Tuple | Set | Dictionary           |
| ---------- | ---- | ----- | --- | -------------------- |
| Ordered    | ✅    | ✅     | ❌   | ✅                    |
| Mutable    | ✅    | ❌     | ✅   | ✅                    |
| Duplicates | ✅    | ✅     | ❌   | **Keys ❌, Values ✅** |
| Indexing   | ✅    | ✅     | ❌   | ❌                    |
| Key-Value  | ❌    | ❌     | ❌   | ✅                    |

### Simple Memory

```text
List       → [ ]
Tuple      → ( )
Set        → {values}
Dictionary → {key:value}
```

---

# 🎯 PART 3 — FINAL SUMMARY TABLE

| Topic                    | Simple Meaning                  | Important Keyword / Concept |
| ------------------------ | ------------------------------- | --------------------------- |
| Dictionary               | Key-value collection            | `key:value`                 |
| Mutable                  | Can change data                 | Add / Update / Delete       |
| Ordered                  | Preserves insertion order       | Python 3.7+                 |
| Keys                     | Unique identifiers              | No duplicate keys           |
| Values                   | Data associated with keys       | Duplicates allowed          |
| Access                   | Get value using key             | `[]`                        |
| Safe Access              | Access without `KeyError`       | `get()`                     |
| Add                      | Add new key-value pair          | `dict[key] = value`         |
| Update                   | Change existing value           | `dict[key] = new_value`     |
| `keys()`                 | Get keys                        | Keys                        |
| `values()`               | Get values                      | Values                      |
| `items()`                | Get key-value pairs             | Key + Value                 |
| `pop()`                  | Remove by key                   | Specific item               |
| `popitem()`              | Remove last inserted item       | Last item                   |
| `del`                    | Delete specific key             | Delete                      |
| `clear()`                | Remove everything               | `{}`                        |
| `setdefault()`           | Add only if missing             | If missing                  |
| `in`                     | Check key existence             | `key in dict`               |
| Nested Dictionary        | Dictionary inside dictionary    | Dict → Dict                 |
| Dictionary of Lists      | Values are lists                | Dict → List                 |
| List of Dictionaries     | List contains dictionaries      | List → Dict                 |
| Dictionary Comprehension | Short dictionary creation       | `{key:value for ...}`       |
| `if`                     | Filter dictionary comprehension | Condition                   |
| `if-else`                | Assign based on condition       | Conditional expression      |
| JSON                     | Common key-value data format    | Dictionary                  |
| Applications             | APIs, JSON, databases, etc.     | Real-world data             |

# 🏆 MUST REMEMBER FOR INTERVIEW

```text
Dictionary
     ↓
Key : Value
```

```text
Key       → Unique
Value     → Duplicate allowed
```

```text
[]        → Direct access
get()     → Safe access
```

```text
keys()    → Keys
values()  → Values
items()   → Key + Value
```

```text
pop()     → Remove by key
popitem() → Remove last item
del       → Delete
clear()   → Remove all
```

```text
setdefault()
      ↓
Add only if key is missing
```

```text
Nested Dictionary
      ↓
Dictionary → Dictionary
```

```text
Dictionary of Lists
      ↓
Dictionary → List
```

```text
List of Dictionaries
      ↓
List → Dictionary
```

```text
Dictionary Comprehension
      ↓
Short way to create Dictionary
```

**Golden interview sentence:**

> **A Python Dictionary is a mutable, ordered collection of unique key-value pairs where keys are used for accessing values.** 
