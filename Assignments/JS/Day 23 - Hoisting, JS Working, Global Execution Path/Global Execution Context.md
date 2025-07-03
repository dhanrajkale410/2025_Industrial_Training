# 🌐 Global Execution Context in JavaScript

The **Global Execution Context (GEC)** is the **default environment** where any JavaScript code starts execution. It is created **automatically** when the JavaScript engine runs your script.

---

## 🧠 What is an Execution Context?

An **Execution Context** is an environment in which JavaScript code is **evaluated and executed**.

There are 3 main types:
1. **Global Execution Context (GEC)**
2. **Function Execution Context (FEC)**
3. **Eval Execution Context** (rarely used)

---

## 🔄 Global Execution Context (GEC)

- Created **only once**, at the start of script execution.
- Represents the **global scope** (outside any function).
- Associated with the `window` object (in browsers).
- Stores:
  - All **global variables**
  - **Functions** declared in the global scope
  - A reference to `this` (which points to `window` in browsers)

---

## 🧪 Example

```javascript
var name = "Dhanraj";

function greet() {
    console.log("Hello " + name);
}

greet();
```
---

> When this code runs:

1. GEC is created
2. Memory is allocated for name and greet
3. Code is executed top to bottom

---

## 🔄 GEC Creation Phases
1. Creation Phase (Memory Allocation)
    - var variables are hoisted and set to undefined
    - Functions are hoisted with their definitions
    - this is initialized (points to window in browser)

2. Execution Phase
    - Code runs line by line
    - Values are assigned
    - Functions are executed (creating new Function Execution Contexts)
---

## 🧠 this keyword in GEC
- In the Global Context, this refers to:
- window (in browser)
- global (in Node.js)

```javascript
console.log(this === window); // true (in browser)
```
---

## 📌 Summary

| Component    | Description                               |
| ------------ | ----------------------------------------- |
| GEC          | The default base execution environment    |
| Created When | JavaScript script starts running          |
| Contains     | Global vars, functions, `this`            |
| Hoisting     | Variables (`undefined`), Functions (full) |
| `this` value | Refers to `window` in browsers            |

---

## Conclusion 
> The GEC is the first thing created and the last thing destroyed when your JavaScript program runs.