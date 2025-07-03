# 🧠 How JavaScript Works Behind the Scenes

JavaScript is a **single-threaded**, **non-blocking**, **asynchronous**, **event-driven** programming language that runs inside the **JavaScript Engine** (e.g., V8 in Chrome, SpiderMonkey in Firefox).

---

## 🧩 Core Components

1. **JavaScript Engine**  
   - Executes JavaScript code
   - Examples: **V8** (Chrome/Node.js), **SpiderMonkey** (Firefox)

2. **Call Stack**  
   - Keeps track of function calls
   - Follows **LIFO** (Last In, First Out)

3. **Memory Heap**  
   - Stores variables and objects in memory

4. **Web APIs (Browser APIs)**  
   - Provided by the browser (e.g., `DOM`, `setTimeout`, `fetch`)
   - Not part of JavaScript itself

5. **Callback Queue / Task Queue**  
   - Stores asynchronous callbacks (e.g., `setTimeout`, event listeners)

6. **Event Loop**  
   - Continuously checks:
     - Is the **call stack** empty?
     - If yes, it moves the **first task** from the **callback queue** to the stack

---

## 🔄 Execution Flow

### 1. **Code runs top to bottom**  
JavaScript parses and executes line by line.

### 2. **Function Calls**  
When a function is called, it’s pushed onto the **call stack**.

### 3. **Async Tasks (e.g., setTimeout)**  
- Sent to **Web APIs**
- When done, they move their callbacks to the **callback queue**
- The **event loop** picks them when the call stack is empty

---

## 🧪 Example

```javascript
console.log("Start");

setTimeout(() => {
    console.log("Timeout done");
}, 1000);

console.log("End");
```
    OUTPUT :
        Start
        End
        Timeout done

> Even though setTimeout is at the top, its callback runs after the main thread is done.
---

## 🧠 Summary

| Concept              | Description                           |
| -------------------- | ------------------------------------- |
| Single-threaded      | Only one thing at a time (Call Stack) |
| Async + Non-blocking | Offloads tasks using Web APIs         |
| Event Loop           | Coordinates execution of callbacks    |
---

## 📦 Bonus: JavaScript Engine Architecture (V8)
1. Parser → Turns code into AST (Abstract Syntax Tree)

2. Interpreter (Ignition) → Quickly runs code

3. Compiler (TurboFan) → Optimizes hot code

4. Garbage Collector → Cleans unused memory
---

# Conclusion
> JavaScript is synchronous at its core but becomes powerful through asynchronous features like callbacks, promises, and the event loop.