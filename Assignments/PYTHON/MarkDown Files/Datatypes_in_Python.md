
# 📄 Python Datatypes

Python has various built-in datatypes to store different kinds of data. Here’s a quick guide with examples.

---

## 🔢 1. Numbers

Python supports:
- **int** : Integer numbers  
- **float** : Floating point numbers (decimals)  
- **complex** : Complex numbers

**Example:**
```python
x = 10        # int
y = 3.14      # float
z = 2 + 3j    # complex

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>
```

---

## 📝 2. String

A string is a sequence of characters enclosed in single, double, or triple quotes.

**Example:**
```python
name = "Alice"
sentence = 'Hello, World!'
multi_line = """This is a 
multi-line string."""

print(name)
print(sentence)
print(multi_line)
```

---

## ✅ 3. Boolean

Boolean datatype represents True or False.

**Example:**
```python
is_active = True
is_logged_in = False

print(is_active)     # True
print(type(is_logged_in))  # <class 'bool'>
```

---

## 📚 4. List

A list stores multiple items in a single variable. Lists are ordered, mutable, and allow duplicates.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
fruits.append("orange")
print(fruits)
```

---

## 📂 5. Tuple

A tuple is like a list but **immutable**.

**Example:**
```python
coordinates = (10, 20)
print(coordinates[1])  # 20
```

---

## 🔑 6. Dictionary

Stores data in key-value pairs.

**Example:**
```python
student = {"name": "John", "age": 21, "grade": "A"}
print(student["name"])  # John
```

---

## 🗂️ 7. Set

A set is an unordered collection of unique items.

**Example:**
```python
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers)  # {1, 2, 3}
```

---

## ✅ Summary

Python datatypes help you store and work with data efficiently! 🚀
