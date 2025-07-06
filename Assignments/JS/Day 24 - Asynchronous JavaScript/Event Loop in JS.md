
# 🔁 JavaScript Event Loop

The **JavaScript Event Loop** is a fundamental concept that explains how JavaScript handles **asynchronous operations** in a **single-threaded** environment.

Despite being single-threaded, JavaScript can perform non-blocking I/O operations like reading files, making API calls, or timers using the Event Loop.

---

## 🧠 Key Concepts

### 1. **Call Stack**
- A LIFO (Last-In, First-Out) stack that tracks function calls.
- When a function is called, it’s pushed onto the stack.
- When it returns, it’s popped off the stack.

### 2. **Web APIs (Browser)**
- Provided by the browser (e.g., `setTimeout`, `DOM events`, `fetch`).
- They handle tasks asynchronously.

### 3. **Callback Queue (Task Queue)**
- Holds the messages (functions) to be executed after async operations complete.

### 4. **Microtask Queue**
- Holds promises and mutation observer callbacks.
- Has **higher priority** than the callback queue.

### 5. **Event Loop**
- Continuously checks if the Call Stack is empty.
- If empty, it moves tasks from the Microtask Queue or Callback Queue into the Call Stack.

---

## 🔄 Event Loop Flow

1. Call Stack runs sync code.
2. Async tasks are sent to Web APIs.
3. Upon completion, their callbacks go into the **Task Queue** (or **Microtask Queue**).
4. Event Loop pushes them into the Call Stack when it's empty.

---

## 📊 Execution Order Example

```js
console.log("Start");

setTimeout(() => {
  console.log("Timeout");
}, 0);

Promise.resolve().then(() => {
  console.log("Promise");
});

console.log("End");
```

### Output:
```
Start
End
Promise
Timeout
```

> `Promise` runs before `setTimeout` because it goes to the **Microtask Queue**, which is prioritized over the **Callback Queue**.

---

## 🕸 Event Loop Visualization

```
+-------------------+           +----------------------+
|   Call Stack      |<----------|  Event Loop          |
+-------------------+           +----------------------+
          ↑                            ↓
+-------------------+           +----------------------+
| Microtask Queue   |           | Callback Queue       |
| (Promises, etc.)  |           | (setTimeout, etc.)   |
+-------------------+           +----------------------+
```

---

## ✅ Summary

| Concept          | Description                                      |
|------------------|--------------------------------------------------|
| Call Stack       | Executes current functions                       |
| Web APIs         | Handle async tasks (e.g., timers, HTTP)          |
| Microtask Queue  | Queue for promises and microtasks                |
| Callback Queue   | Queue for timers and events                      |
| Event Loop       | Manages task execution between stack and queues |

---

> 💡 Mastering the Event Loop helps you understand timing, async behavior, and performance in JavaScript applications.