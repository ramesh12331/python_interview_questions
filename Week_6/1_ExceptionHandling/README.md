# 📘 PYTHON FILE HANDLING — FINAL REVISION

Based on your uploaded **Final Summary — Python File Handling, Binary & Serialization**. 

As you requested:

**PART 1 → Questions & Answers**
**PART 2 → Questions + Answers + Basic Code + Output + Explanation**
**PART 3 → Final Summary Table**

---

# 🟢 PART 1 — IMPORTANT QUESTIONS & ANSWERS

## 📂 File Handling

### Q1. What is File Handling in Python?

**Answer:**
**File handling means creating, opening, reading, writing, appending, and managing files using Python.**

---

### Q2. What are the common file modes?

**Answer:**

```text
r  → Read
w  → Write
a  → Append
x  → Create
rb → Read Binary
wb → Write Binary
```

---

### Q3. What does `with` do in file handling?

**Answer:**
**`with` automatically closes the file after the block finishes.**

---

# 📖 Reading Files

### Q4. What does `read()` do?

**Answer:**
**`read()` reads file content.**

---

### Q5. What does `readline()` do?

**Answer:**
**`readline()` reads one line from the file.**

---

### Q6. What does `readlines()` do?

**Answer:**
**`readlines()` reads lines into a list.**

---

### Q7. What is the difference between `read()`, `readline()` and `readlines()`?

**Answer:**

```text
read()      → ALL content
readline()  → ONE line
readlines() → Lines as LIST
```

---

# ✍️ Writing & Appending

### Q8. What is the difference between `"w"` and `"a"`?

**Answer:**

```text
"w" → Write / Overwrite
"a" → Add content at the end
```

**`w` can overwrite existing content, while `a` adds content at the end.**

---

### Q9. What does `write()` do?

**Answer:**
**`write()` writes content into a file.**

---

# 🎯 File Pointer

### Q10. What does `tell()` do?

**Answer:**
**`tell()` returns the current file-pointer position.**

---

### Q11. What does `seek()` do?

**Answer:**
**`seek()` moves the file pointer to a specified position.**

---

### Q12. What is the shortcut for `tell()` and `seek()`?

**Answer:**

```text
tell() → WHERE am I? 📍
seek() → GO there 🎯
```

---

# 📊 CSV

### Q13. What is CSV?

**Answer:**
**CSV stands for Comma-Separated Values. It is commonly used for table-like data.**

---

### Q14. What does `writerow()` do?

**Answer:**
**`writerow()` writes one row.**

---

### Q15. What does `writerows()` do?

**Answer:**
**`writerows()` writes multiple rows.**

---

### Q16. What does `csv.reader()` do?

**Answer:**
**`csv.reader()` is used to read CSV rows.**

---

# 💾 Binary Files

### Q17. What is a Binary File?

**Answer:**
**Binary data is handled as bytes.**

Examples include:

```text
Images
Audio
Video
PDF
EXE
```

---

### Q18. What is the difference between text and binary files?

**Answer:**

```text
Text   → Characters
Binary → Bytes
```

Modes:

```text
r  → Read Text
w  → Write Text

rb → Read Binary
wb → Write Binary
```

---

# 📦 Serialization

### Q19. What is Serialization?

**Answer:**
**Serialization means converting a Python object into a format suitable for storage.**

Memory trick:

```text
Python Object
     ↓
Serialization
     ↓
Storage
```

**Serialization = PACK 📦**

---

### Q20. What is Deserialization?

**Answer:**
**Deserialization means converting stored data back into a Python object.**

```text
Storage
   ↓
Deserialization
   ↓
Python Object
```

**Deserialization = UNPACK 📤**

---

### Q21. What is the difference between Serialization and Deserialization?

**Answer:**

```text
Serialization
Python → Storage

Deserialization
Storage → Python
```

---

### Q22. Which modules are mentioned for Serialization?

**Answer:**

```text
json
pickle
```

---

# 💻 PART 2 — QUESTIONS + ANSWERS + BASIC CODE

## Q1. How do you open and read a file?

### Answer

**Use `open()` with `"r"` mode and `read()` to read the content.**

### Basic Code

```python
with open("sample.txt", "r") as f:
    data = f.read()

print(data)
```

### Output

If `sample.txt` contains:

```text
Hello Python
```

Output:

```text
Hello Python
```

### Simple Explanation

```text
open() → Open file
"r"    → Read mode
read() → Read content
with   → Automatically close
```

---

## Q2. How do you write data into a file?

### Answer

**Use `"w"` mode and the `write()` method.**

### Basic Code

```python
with open("sample.txt", "w") as f:
    f.write("Hello Python")
```

### Output

`sample.txt` contains:

```text
Hello Python
```

### Simple Explanation

```text
"w" → Write
write() → Write content
```

**If the file already has content, `"w"` can overwrite it.**

---

## Q3. How do you append data to a file?

### Answer

**Use `"a"` mode. It adds content at the end.**

### Basic Code

```python
with open("sample.txt", "a") as f:
    f.write(" Python")
```

### Output

If the file initially contains:

```text
Hello
```

After execution:

```text
Hello Python
```

### Simple Explanation

```text
"a"
 ↓
Append
 ↓
Add at end
```

---

## Q4. How do you read one line?

### Answer

**Use `readline()`.**

### Basic Code

```python
with open("sample.txt", "r") as f:
    line = f.readline()

print(line)
```

### Output

```text
Hello Python
```

### Simple Explanation

```text
readline()
    ↓
ONE LINE
```

---

## Q5. How do you read all lines into a list?

### Answer

**Use `readlines()`.**

### Basic Code

```python
with open("sample.txt", "r") as f:
    lines = f.readlines()

print(lines)
```

Suppose the file contains:

```text
Python
SQL
HTML
```

### Output

```python
['Python\n', 'SQL\n', 'HTML']
```

### Simple Explanation

```text
readlines()
     ↓
All lines
     ↓
List
```

---

## Q6. How do you find the current file-pointer position?

### Answer

**Use `tell()`.**

### Basic Code

```python
with open("sample.txt", "r") as f:
    print(f.tell())
```

### Output

```text
0
```

### Simple Explanation

At the beginning:

```text
Pointer
   ↓
Python
```

So:

```python
f.tell()
```

tells us **where the pointer currently is**.

---

## Q7. How do you move the file pointer?

### Answer

**Use `seek()`.**

### Basic Code

```python
with open("sample.txt", "r") as f:

    f.seek(5)

    print(f.read())
```

Suppose:

```text
Hello Python
```

### Output

```text
 Python
```

### Simple Explanation

```python
f.seek(5)
```

moves the pointer to position `5`.

Memory:

```text
tell() → WHERE am I? 📍
seek() → GO there 🎯
```

---

## Q8. What is CSV?

### Answer

**CSV means Comma-Separated Values and is useful for table-like data.**

### Basic Code

```python
import csv

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["id", "name", "age"])
    writer.writerow([101, "Ramesh", 25])
```

### Output

`students.csv`:

```text
id,name,age
101,Ramesh,25
```

### Simple Explanation

CSV stores data like a table:

```text
id | name   | age
---|--------|----
101| Ramesh | 25
```

---

## Q9. What is the difference between `writerow()` and `writerows()`?

### Answer

```text
writerow()
    ↓
ONE row

writerows()
    ↓
MANY rows
```

### Basic Code

```python
import csv

rows = [
    [101, "Ramesh"],
    [102, "Rahul"],
    [103, "Ajay"]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerows(rows)
```

### Output

```text
101,Ramesh
102,Rahul
103,Ajay
```

### Simple Explanation

```text
writerow  → one row
writerows → multiple rows
```

---

## Q10. How do you read a CSV file?

### Answer

**Use `csv.reader()`.**

### Basic Code

```python
import csv

with open("students.csv", "r") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)
```

### Output

```text
['101', 'Ramesh']
['102', 'Rahul']
['103', 'Ajay']
```

### Simple Explanation

```text
CSV File
   ↓
csv.reader()
   ↓
Rows
```

---

## Q11. What is a Binary File?

### Answer

**Binary data is handled as bytes.**

Examples:

```text
🖼️ Image
🎵 Audio
🎬 Video
📕 PDF
⚙️ EXE
```

### Basic Code

```python
with open("image.jpg", "rb") as f:
    data = f.read()

print(data)
```

### Output

You will get binary/bytes data, for example:

```text
b'\xff\xd8\xff...'
```

### Simple Explanation

```text
"r"  → Text Read
"rb" → Binary Read
```

---

## Q12. What is Serialization?

### Answer

**Serialization converts a Python object into a format suitable for storage.**

### Basic Code

Using the `json` module mentioned in your notes:

```python
import json

data = {
    "name": "Ramesh",
    "age": 25
}

with open("data.json", "w") as f:
    json.dump(data, f)
```

### Output

`data.json` contains stored JSON data:

```json
{
    "name": "Ramesh",
    "age": 25
}
```

### Simple Explanation

```text
Python Object
     ↓
Serialization
     ↓
Stored Format
```

**Serialization = PACK 📦**

---

## Q13. What is Deserialization?

### Answer

**Deserialization converts stored data back into a Python object.**

### Basic Code

```python
import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)
```

### Output

```python
{'name': 'Ramesh', 'age': 25}
```

### Simple Explanation

```text
Stored JSON
     ↓
Deserialization
     ↓
Python Object
```

**Deserialization = UNPACK 📤**

---

## Q14. What is the difference between Serialization and Deserialization?

### Answer

```text
Serialization
     ↓
Python → Storage

Deserialization
     ↓
Storage → Python
```

### Basic Code

```python
import json

data = {"name": "Ramesh"}

# Serialization
with open("data.json", "w") as f:
    json.dump(data, f)

# Deserialization
with open("data.json", "r") as f:
    new_data = json.load(f)

print(new_data)
```

### Output

```text
{'name': 'Ramesh'}
```

### Simple Explanation

```text
🐍 Python Object
       │
       ▼
   Serialization
       │
       ▼
   💾 Storage
       │
       ▼
 Deserialization
       │
       ▼
🐍 Python Object
```

---

# 🎯 MOST IMPORTANT INTERVIEW SHORTCUTS

```text
open()       → Open file

read()       → Read ALL

readline()   → Read ONE LINE

readlines()  → Read LINES → LIST

write()      → Write content

r            → Read

w            → Write / Overwrite

a            → Append

x            → Create

rb           → Read Binary

wb           → Write Binary

tell()       → Current pointer position

seek()       → Move pointer

CSV          → Table-like data

writerow()   → ONE row

writerows()  → MANY rows

csv.reader() → Read CSV

Serialization
Python → Storage

Deserialization
Storage → Python

json         → Serialization module mentioned

pickle       → Serialization module mentioned
```

---

# 📊 PART 3 — FINAL SUMMARY TABLE

| Topic           | Simple Meaning                 | Important Keyword / Concept |
| --------------- | ------------------------------ | --------------------------- |
| File Handling   | Work with files                | Open / Read / Write         |
| `open()`        | Opens a file                   | Open                        |
| `read()`        | Reads all content              | ALL                         |
| `readline()`    | Reads one line                 | ONE LINE                    |
| `readlines()`   | Reads lines as list            | LIST                        |
| `write()`       | Writes data                    | Write                       |
| `r`             | Read text                      | Read                        |
| `w`             | Write / overwrite              | Replace                     |
| `a`             | Add at end                     | Append                      |
| `x`             | Create a new file              | Create                      |
| `rb`            | Read binary data               | Bytes                       |
| `wb`            | Write binary data              | Bytes                       |
| `with`          | Automatically closes file      | Auto Close                  |
| `tell()`        | Current pointer position       | WHERE?                      |
| `seek()`        | Moves pointer                  | GO THERE                    |
| CSV             | Comma-Separated Values         | Tabular Data                |
| `writerow()`    | Writes one row                 | ONE                         |
| `writerows()`   | Writes multiple rows           | MANY                        |
| `csv.reader()`  | Reads CSV rows                 | Read                        |
| Binary File     | Data handled as bytes          | Bytes                       |
| Serialization   | Python → Storage               | PACK 📦                     |
| Deserialization | Storage → Python               | UNPACK 📤                   |
| `json`          | Serialization module mentioned | JSON                        |
| `pickle`        | Serialization module mentioned | Pickle                      |

---

# 🏆 FINAL MASTER MEMORY

```text
                 🐍 PYTHON FILE HANDLING
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
     📖 READ           ✍️ WRITE          💾 BINARY
        │                 │                 │
    read()              write()          rb / wb
    readline()             │
    readlines()            ▼
        │              w / a / x
        │
        ▼
    🎯 POINTER
        │
   tell() / seek()
        │
        ▼
      📊 CSV
        │
 writerow / writerows
 csv.reader()
        │
        ▼
   📦 SERIALIZATION
        │
 Python → Storage
        │
        ▼
 🔄 DESERIALIZATION
        │
 Storage → Python
```

### 🔥 10 MUST-REMEMBER INTERVIEW POINTS

1. **`read()` → reads all content**
2. **`readline()` → reads one line**
3. **`readlines()` → reads lines as a list**
4. **`w` → write/overwrite**
5. **`a` → append at the end**
6. **`with` → automatically closes the file**
7. **`tell()` → current pointer position**
8. **`seek()` → moves the pointer**
9. **CSV → table-like data**
10. **Serialization = Python → Storage; Deserialization = Storage → Python** 
