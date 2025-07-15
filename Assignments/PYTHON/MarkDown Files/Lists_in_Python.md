
# 📚 Python Lists

A **List** is a built-in Python data structure that stores an ordered collection of items. Lists are **mutable** (changeable) and can hold items of different datatypes.

---

## ✅ Creating a List

```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
```

---

## 🔍 Accessing List Items

Use **indexing** and **slicing**.

```python
print(fruits[0])    # apple
print(fruits[-1])   # cherry
print(fruits[1:3])  # ['banana', 'cherry']
```

---

## ✏️ Common List Methods

| Method          | Description                               | Example                                       |
|-----------------|-------------------------------------------|-----------------------------------------------|
| `append()`      | Adds an item to the end                   | `fruits.append("orange")`                     |
| `insert()`      | Inserts item at specified index           | `fruits.insert(1, "mango")`                   |
| `extend()`      | Adds multiple items                       | `fruits.extend(["grape", "melon"])`           |
| `remove()`      | Removes first occurrence of item          | `fruits.remove("banana")`                     |
| `pop()`         | Removes item at index (last by default)   | `fruits.pop()` or `fruits.pop(0)`             |
| `clear()`       | Removes all items                         | `fruits.clear()`                              |
| `index()`       | Returns index of first occurrence         | `fruits.index("apple")`                       |
| `count()`       | Counts how many times an item appears     | `fruits.count("apple")`                       |
| `sort()`        | Sorts the list                            | `numbers.sort()`                              |
| `reverse()`     | Reverses the list                         | `fruits.reverse()`                            |
| `copy()`        | Returns a shallow copy                    | `new_list = fruits.copy()`                    |

---

## 🔁 Looping through a List

```python
for fruit in fruits:
    print(fruit)
```

---

## 🧩 Nested Lists

Lists can contain other lists.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # 6
```

---

## ✅ Summary

- **Lists are mutable** and flexible.
- **Commonly used** for storing and manipulating ordered data.

Happy Coding! 🚀
