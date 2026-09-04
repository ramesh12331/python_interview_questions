# 📘 NEXT — SERIALIZATION & DESERIALIZATION: INTERVIEW REVISION

We’ll continue in your exact format: **Part 1 → Part 2 → Part 3**. This is based on your uploaded material covering **JSON, custom objects, Pickle/Unpickle, and multiple `Bank` objects**. 

# 🟢 PART 1 — IMPORTANT QUESTIONS & ANSWERS

### Q1. What is Serialization?

**Answer:**
**Serialization is converting Python data/object into a format that can be stored in a file.**

```text
Python Object → Stored Format
```

---

### Q2. What is Deserialization?

**Answer:**
**Deserialization is converting stored data back into Python data/object form.**

```text
Stored Format → Python Object
```

---

### Q3. What is JSON Serialization?

**Answer:**
**JSON serialization converts Python data into JSON format for storage.**

---

### Q4. Which function is used to serialize data into JSON?

**Answer:**

```python
json.dump()
```

**`json.dump()` is used to save Python data into a JSON file.**

---

### Q5. Which function is used for JSON Deserialization?

**Answer:**

```python
json.load()
```

**`json.load()` reads JSON data from a file and converts it back to Python data.**

---

### Q6. What does `indent=4` do?

**Answer:**
**`indent=4` makes the JSON output formatted and easier to read.**

---

### Q7. Can we directly serialize a custom class object using `json.dump()`?

**Answer:**
**Not directly in the example from your notes.** A custom `Bank` object gives a `TypeError` because it is not JSON serializable.

---

### Q8. How can we convert a custom object for JSON serialization?

**Answer:**
Your notes show two approaches:

```text
Object
   ↓
__dict__
   ↓
Dictionary
   ↓
JSON
```

or using:

```python
default=get_info
```

---

### Q9. What is Pickling?

**Answer:**
**Pickling is serialization using Python's `pickle` module.**

---

### Q10. What is Unpickling?

**Answer:**
**Unpickling is reading the pickled data back into Python object form.**

---

### Q11. Which functions are used for Pickling and Unpickling?

**Answer:**

```text
pickle.dump() → Pickling / Save
pickle.load() → Unpickling / Load
```

---

### Q12. Which modes are used with Pickle?

**Answer:**

```text
wb → Write Binary
rb → Read Binary
```

---

### Q13. What is `__dict__`?

**Answer:**
**`__dict__` gives the instance attributes of an object in dictionary form.**

---

### Q14. How can we store multiple objects?

**Answer:**
Create objects inside a loop, add them to a list, and then serialize the list.

```text
Input
 ↓
Object
 ↓
List
 ↓
Serialize
 ↓
File
```

---

# 💻 PART 2 — QUESTIONS + ANSWERS + BASIC CODE

## Q1. How do you serialize a Python dictionary using JSON?

### Answer

**Use `json.dump()` to store the dictionary in a JSON file.**

### Basic Code

```python
import json

data = {
    "name": "Ramesh",
    "age": 30
}

with open("data.json", "w") as f:
    json.dump(data, f)
```

### Output

`data.json`:

```json
{
    "name": "Ramesh",
    "age": 30
}
```

### Simple Explanation

```text
Dictionary
    ↓
json.dump()
    ↓
data.json
```

---

## Q2. How do you deserialize JSON data?

### Answer

**Use `json.load()` to read JSON data back into Python.**

### Basic Code

```python
import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)
```

### Output

```text
{'name': 'Ramesh', 'age': 30}
```

### Simple Explanation

```text
JSON File
   ↓
json.load()
   ↓
Python Dictionary
```

---

## Q3. What does `indent=4` do?

### Answer

**It formats JSON so that it is easier for humans to read.**

### Basic Code

```python
import json

data = {
    "name": "Ramesh",
    "age": 30
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

### Output

```json
{
    "name": "Ramesh",
    "age": 30
}
```

### Simple Explanation

```text
indent=4
    ↓
Pretty / formatted JSON
```

---

## Q4. Why does normal `write()` fail with a dictionary?

### Answer

**The text `write()` method expects a string, not a dictionary.**

### Basic Code

```python
data = {
    "name": "Ramesh",
    "age": 30
}

with open("data.txt", "w") as f:
    f.write(data)
```

### Output

```text
TypeError
```

### Simple Explanation

Your notes show:

```text
write()
  ↓
expects string
```

But:

```text
data
 ↓
dictionary
```

So we use JSON serialization:

```python
json.dump(data, f)
```

---

## Q5. Can `json.dump()` directly store a custom `Bank` object?

### Answer

**Not directly in the example from your notes.** It produces a `TypeError` because the custom object is not JSON serializable.

### Basic Code

```python
import json

class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance


a = Bank("Ramesh", 30, 50000)

with open("bank.json", "w") as f:
    json.dump(a, f)
```

### Output

```text
TypeError:
Object of type Bank is not JSON serializable
```

### Simple Explanation

JSON understands standard data structures such as dictionaries, but the `Bank` object in your example needs to be converted first.

---

## Q6. How do you use `__dict__` for JSON serialization?

### Answer

**`__dict__` converts the object's instance attributes into dictionary form.**

### Basic Code

```python
import json

class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance


a = Bank("Ramesh", 30, 50000)

print(a.__dict__)
```

### Output

```text
{'name': 'Ramesh', 'age': 30, 'balance': 50000}
```

Now serialize it:

```python
with open("bank.json", "w") as f:
    json.dump(a.__dict__, f, indent=4)
```

### Simple Explanation

```text
Bank Object
     ↓
__dict__
     ↓
Dictionary
     ↓
json.dump()
     ↓
JSON File
```

---

## Q7. How can `default=get_info` be used?

### Answer

Your notes show a function that converts the object into a dictionary.

### Basic Code

```python
import json

class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance


def get_info(obj):
    return {
        "name": obj.name,
        "age": obj.age,
        "balance": obj.balance
    }


a = Bank("Ramesh", 30, 50000)

with open("bank.json", "w") as f:
    json.dump(a, f, default=get_info, indent=4)
```

### Output

```json
{
    "name": "Ramesh",
    "age": 30,
    "balance": 50000
}
```

### Simple Explanation

```text
Bank Object
    ↓
get_info()
    ↓
Dictionary
    ↓
json.dump()
    ↓
JSON
```

---

# 🥒 PICKLE

## Q8. How do you pickle a Python object?

### Answer

**Use `pickle.dump()` with binary write mode `wb`.**

### Basic Code

```python
import pickle

class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance


a = Bank("Ramesh", 30, 50000)

with open("bank.pkl", "wb") as f:
    pickle.dump(a, f)
```

### Output

```text
bank.pkl
```

The object is stored in the pickle file.

### Simple Explanation

```text
Bank Object
     ↓
pickle.dump()
     ↓
bank.pkl
```

**Pickle directly stores the object in the example from your notes.**

---

## Q9. How do you unpickle an object?

### Answer

**Use `pickle.load()` with binary read mode `rb`.**

### Basic Code

```python
import pickle

with open("bank.pkl", "rb") as f:
    data = pickle.load(f)

print(data.name)
print(data.age)
print(data.balance)
```

### Output

```text
Ramesh
30
50000
```

### Simple Explanation

```text
bank.pkl
   ↓
pickle.load()
   ↓
Bank Object
```

---

## Q10. Why do we use `wb` with Pickle?

### Answer

**`wb` means Write Binary.**

```text
w → Write
b → Binary

wb → Write Binary
```

### Basic Code

```python
with open("bank.pkl", "wb") as f:
    pickle.dump(a, f)
```

### Simple Explanation

Your Pickle example stores the object using **binary write mode**.

---

## Q11. Why do we use `rb` with Pickle?

### Answer

**`rb` means Read Binary.**

```text
r → Read
b → Binary

rb → Read Binary
```

### Basic Code

```python
with open("bank.pkl", "rb") as f:
    data = pickle.load(f)
```

---

# 🔟 MULTIPLE OBJECTS

## Q12. How do you store multiple `Bank` objects?

### Answer

**Create multiple objects inside a loop, append them to a list, and serialize the list.**

### Basic Code

```python
import pickle

class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance


customers = []

for i in range(3):

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    balance = float(input("Enter Balance: "))

    obj = Bank(name, age, balance)

    customers.append(obj)


with open("customers.pkl", "wb") as f:
    pickle.dump(customers, f)
```

### Output

Suppose input:

```text
Enter Name: Ramesh
Enter Age: 30
Enter Balance: 50000

Enter Name: Rahul
Enter Age: 25
Enter Balance: 40000

Enter Name: Ajay
Enter Age: 28
Enter Balance: 60000
```

The file contains a **list of `Bank` objects**.

### Simple Explanation

```text
Input
 ↓
Bank Object
 ↓
append()
 ↓
customers list
 ↓
pickle.dump()
 ↓
customers.pkl
```

---

## Q13. How do you store multiple objects in JSON?

### Answer

For the JSON pattern in your notes, **convert each object to a dictionary using `__dict__`**, append those dictionaries to a list, and then use `json.dump()`.

### Basic Code

```python
import json

class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance


customers = []

for i in range(3):

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    balance = float(input("Enter Balance: "))

    obj = Bank(name, age, balance)

    customers.append(obj.__dict__)


with open("customers.json", "w") as f:
    json.dump(customers, f, indent=4)
```

### Output

```json
[
    {
        "name": "Ramesh",
        "age": 30,
        "balance": 50000.0
    },
    {
        "name": "Rahul",
        "age": 25,
        "balance": 40000.0
    }
]
```

### Simple Explanation

```text
Bank Object
    ↓
__dict__
    ↓
Dictionary
    ↓
List
    ↓
json.dump()
    ↓
customers.json
```

---

## Q14. How do you read multiple Pickled objects?

### Answer

**Load the list using `pickle.load()` and then use a loop to access each object.**

### Basic Code

```python
import pickle

with open("customers.pkl", "rb") as f:
    customers = pickle.load(f)


for customer in customers:
    print(customer.name)
    print(customer.age)
    print(customer.balance)
```

### Output

```text
Ramesh
30
50000

Rahul
25
40000

Ajay
28
60000
```

### Simple Explanation

```text
customers.pkl
      ↓
pickle.load()
      ↓
List of objects
      ↓
for loop
      ↓
Each Bank object
```

---

# ⭐ MOST IMPORTANT DIFFERENCE

## JSON vs Pickle

| JSON                                           | Pickle                                               |
| ---------------------------------------------- | ---------------------------------------------------- |
| `import json`                                  | `import pickle`                                      |
| `json.dump()`                                  | `pickle.dump()`                                      |
| `json.load()`                                  | `pickle.load()`                                      |
| Uses `w`                                       | Uses `wb`                                            |
| Uses `r`                                       | Uses `rb`                                            |
| Custom object needs conversion in your example | Object can be stored directly in your Pickle example |
| `.json`                                        | `.pkl`                                               |
| `__dict__` can convert object to dictionary    | Stores the object                                    |

---

# 🎯 INTERVIEW PRIORITY

### 🔥 Very Important

```text
1. Serialization
2. Deserialization
3. json.dump()
4. json.load()
5. __dict__
6. pickle.dump()
7. pickle.load()
8. wb vs rb
9. JSON vs Pickle
10. Multiple objects using list + loop
```

### 🧠 One-Line Answers

> **Serialization = Python Object → Storage**

> **Deserialization = Storage → Python Object**

> **`json.dump()` = Save JSON**

> **`json.load()` = Load JSON**

> **`pickle.dump()` = Pickle/Save Object**

> **`pickle.load()` = Unpickle/Load Object**

> **`__dict__` = Object attributes → Dictionary**

> **`wb` = Write Binary**

> **`rb` = Read Binary**

---

# 📊 PART 3 — FINAL SUMMARY TABLE

| Topic                   | Simple Meaning                  | Important Keyword |
| ----------------------- | ------------------------------- | ----------------- |
| Serialization           | Python → Stored format          | PACK 📦           |
| Deserialization         | Stored format → Python          | UNPACK 🔄         |
| JSON                    | Store structured data           | `json`            |
| `json.dump()`           | Save JSON data                  | SAVE              |
| `json.load()`           | Load JSON data                  | LOAD              |
| `indent=4`              | Format JSON                     | Readable          |
| Custom Object           | User-defined Python object      | `Bank`            |
| `__dict__`              | Object attributes as dictionary | Object → Dict     |
| `default=get_info`      | Convert custom object for JSON  | Converter         |
| Pickling                | Serialization using pickle      | `pickle.dump()`   |
| Unpickling              | Loading pickled data            | `pickle.load()`   |
| `wb`                    | Write Binary                    | Pickle Save       |
| `rb`                    | Read Binary                     | Pickle Load       |
| `pickle.dump()`         | Store object                    | SAVE              |
| `pickle.load()`         | Restore object                  | LOAD              |
| Multiple Objects        | Objects stored in a list        | Loop + List       |
| JSON Multiple Objects   | List of dictionaries            | `__dict__`        |
| Pickle Multiple Objects | List of objects                 | `pickle`          |

# 🏆 MASTER MEMORY

```text
             🐍 PYTHON OBJECT
                    │
             ┌──────┴──────┐
             ▼             ▼
          🗂️ JSON        🥒 PICKLE
             │             │
        __dict__       dump()
             │             │
             ▼             ▼
       Dictionary        Object
             │             │
        json.dump()    pickle.dump()
             │             │
             ▼             ▼
        📄 .json         📦 .pkl
             │             │
        json.load()    pickle.load()
             │             │
             ▼             ▼
       Python Data      Python Object
```

**Golden rule:**

> 📦 **Serialization = PACK → Save**
> 🔄 **Deserialization = UNPACK → Load**
> 🗂️ **JSON = `dump()` / `load()`**
> 🥒 **Pickle = `dump()` / `load()` + binary modes `wb` / `rb`**. 
