# 📚 Python Tuples

A **Tuple** is a built-in Python data structure that stores an ordered collection of items. Tuples are **immutable** (unchangeable) and can hold items of different datatypes.

---

## ✅ Creating a Tuple

```python
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")
mixed = (1, "hello", 3.14, True)
```

> Single-element Tuple:
To create a single-element tuple, add a trailing comma:

## 🔍 Accessing Tuple Items
Use indexing and slicing:

```python 
print(fruits[0])    # apple
print(fruits[-1])   # cherry
print(fruits[1:3])  # ('banana', 'cherry')
```

## ⚡ Tuple Methods
Tuples have only two built-in methods:

| Method    | Description                             | Example                  |
| --------- | --------------------------------------- | ------------------------ |
| `count()` | Counts how many times a value appears   | `fruits.count("apple")`  |
| `index()` | Finds the index of the first occurrence | `fruits.index("banana")` |


## 🔁 Looping through a Tuple

```python
for fruit in fruits:
    print(fruit)
```

## 🧩 Nested Tuples
Tuples can contain other tuples or lists:

```python
nested = ("Alice", [1, 2, 3], (4, 5, 6))
print(nested[1])     # [1, 2, 3]
print(nested[2][1])  # 5
```

## 🔄 Convert Between Tuple and List
Since tuples are immutable, convert them to a list if you need to change them:

```python 
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list.append(4)
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3, 4)
```

## ✅ Why Use Tuples?
- Immutable: Data can’t be changed accidentally.

- Faster: More efficient than lists for fixed data.

- Hashable: Can be used as keys in dictionaries.

## 🗒️ Summary
✔️ Tuples are ordered and immutable.
✔️ Use for fixed, unchangeable data collections.
✔️ Lightweight and fast.