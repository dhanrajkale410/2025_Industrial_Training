# 📚 Python Strings
A String (str) in Python is an immutable sequence of Unicode characters. Strings are widely used to store text data.

---

## ✅ Creating Strings

```python
name = "Dhanraj"
greeting = 'Hello, World!'
multi_line = """This is a
multi-line string."""
```

## 🔍 Accessing String Characters
Use indexing and slicing:

```python
text = "Python"

print(text[0])    # P
print(text[-1])   # n
print(text[1:4])  # yth
```

## ⚡ Common String Methods

| Method         | Description                                   | Example                                   |
| -------------- | --------------------------------------------- | ----------------------------------------- |
| `lower()`      | Converts to lowercase                         | `"HELLO".lower()` ➜ `'hello'`             |
| `upper()`      | Converts to uppercase                         | `"hello".upper()` ➜ `'HELLO'`             |
| `title()`      | Capitalizes first letter of each word         | `"hello world".title()` ➜ `'Hello World'` |
| `strip()`      | Removes leading/trailing whitespace           | `"  hello  ".strip()` ➜ `'hello'`         |
| `replace()`    | Replaces substring                            | `"Hello".replace("H", "J")` ➜ `'Jello'`   |
| `split()`      | Splits string into list                       | `"a,b,c".split(",")` ➜ `['a', 'b', 'c']`  |
| `join()`       | Joins list into string                        | `"-".join(['a', 'b', 'c'])` ➜ `'a-b-c'`   |
| `find()`       | Finds first occurrence index, -1 if not found | `"hello".find("e")` ➜ `1`                 |
| `count()`      | Counts occurrences of substring               | `"hello".count("l")` ➜ `2`                |
| `startswith()` | Checks if string starts with a value          | `"hello".startswith("he")` ➜ `True`       |
| `endswith()`   | Checks if string ends with a value            | `"hello".endswith("lo")` ➜ `True`         |


## 🔁 Looping through a String

```python
word = "Python"
for char in word:
    print(char)
```

## 🧩 String Formatting
Python has powerful formatting options:

1. f-strings :

    ```python
    name = "Dhanraj"
    age = 18
    print(f"My name is {name} and I am {age} years old.")
    ```
2. format() method:

    ```python
    text = "Hello, {}!".format("World")
    print(text)
    ```

## ⚠️ Strings are Immutable
You cannot change a string directly:

```python 
word = "hello"
# word[0] = "H"  # ❌ This will cause an error
```

To change, you must create a new string:

```python
word = "hello"
new_word = "H" + word[1:]
print(new_word)  # Hello
```

## 🗒️ Summary
- Strings are immutable sequences of characters.
- They support indexing, slicing, and many methods for text operations.
- Use f-strings or format() for inserting variables.