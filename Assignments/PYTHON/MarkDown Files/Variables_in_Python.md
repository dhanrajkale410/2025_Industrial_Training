# 📚 Python Variables
A variable is a name that refers to a value stored in memory. In Python, variables are created when you assign a value to them — you don’t need to declare a type explicitly.

---

## ✅ Creating Variables
Python uses the = operator to assign a value to a variable.

```python
x = 18
name = "Dhanraj"
grade = 90.71
is_active = True
```

## ⚡ Key Points

> Dynamic Typing:
Python automatically decides the variable type based on the value assigned. You don’t write int x or string name.

```python
a = 5      # int
a = "Hi"   # Now 'a' is a string
```

> No Declaration Needed:
Just assign a value and the variable is created.

> Case-Sensitive:
Age and age are different variables.

> Naming Rules:

- Can contain letters, numbers, and underscores (_).

- Cannot start with a number.

- Avoid reserved keywords (if, class, True, etc.).

Valid names:

```python
user_name = "Dhanraj"
age1 = 25
```

Invalid names:
```python
1st_value = 10    # ❌ starts with a number
class = "Math"    # ❌ 'class' is a keyword
```

## 🔁 Updating Variables
You can reassign variables anytime:

```python
score = 50
score = score + 10   # Now score is 60
```

## 🧩 Multiple Assignments
Python allows assigning multiple variables in one line:

```python
x, y, z = 1, 2, 3
a = b = c = 5  # All three get 5
```

## 🧮 Type Checking
Use type() to check a variable’s type:

```python 
x = 10
print(type(x))  # <class 'int'>

name = "Dhanraj"
print(type(name))  # <class 'str'>
```

## 🗒️ Summary
- Variables store data in memory.
- Python uses dynamic typing — no type declarations needed.
- Variable names should be meaningful, valid, and follow rules.
- Use type() to check types.