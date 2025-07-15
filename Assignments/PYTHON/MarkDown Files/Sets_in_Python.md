# 📚 Python Sets
A Set is an unordered, unindexed collection of unique elements in Python. Sets are mutable but can only contain hashable (immutable) elements.

---

## ✅ Creating a Set

```python
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}
empty_set = set()  # Correct way to create an empty set
```

---

## ⚡ Key Properties
- **Unordered**: No indexing or slicing
- **No duplicates**: All elements must be unique
- **Mutable**: Can add/remove items
- **Unindexed**: Cannot access by position

---

## 🔍 Common Set Methods

| Method                   | Description                                             | Example                                |     |
| ------------------------ | ------------------------------------------------------- | -------------------------------------- | --- |
| `add()`                  | Adds an element to the set                              | `fruits.add("orange")`                 |     |
| `update()`               | Adds multiple elements                                  | `fruits.update(["grape", "melon"])`    |     |
| `remove()`               | Removes a specified element (raises error if not found) | `fruits.remove("banana")`              |     |
| `discard()`              | Removes a specified element (no error if not found)     | `fruits.discard("banana")`             |     |
| `pop()`                  | Removes and returns an arbitrary element                | `fruits.pop()`                         |     |
| `clear()`                | Removes all elements                                    | `fruits.clear()`                       |     |
| `union()`                | Returns union of two sets                               | `A.union(B)` or \`A                    | B\` |
| `intersection()`         | Returns common elements                                 | `A.intersection(B)` or `A & B`         |     |
| `difference()`           | Returns elements only in the first set                  | `A.difference(B)` or `A - B`           |     |
| `symmetric_difference()` | Returns elements not common to both sets                | `A.symmetric_difference(B)` or `A ^ B` |     |
| `issubset()`             | Checks if set is a subset of another                    | `A.issubset(B)`                        |     |
| `issuperset()`           | Checks if set is a superset of another                  | `A.issuperset(B)`                      |     |
| `isdisjoint()`           | Checks if sets have no common elements                  | `A.isdisjoint(B)`                      |     |

---

## ✅ Example

```python 
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Union: {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersection: {3, 4}
print(A - B)  # Difference: {1, 2}
print(A ^ B)  # Symmetric Difference: {1, 2, 5, 6}
```
---

## 🔁 Looping through a Set

```python
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)
```
---

## 🗒️ Summary
- Sets store unique, unordered items
- Useful for membership tests, removing duplicates, and set operations like union, intersection, and difference
- Elements must be immutable