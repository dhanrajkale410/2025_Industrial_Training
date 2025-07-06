
# ⚡ JavaScript `async/await`

`async` and `await` are modern JavaScript features introduced in **ES2017** to simplify working with asynchronous code, making it look and behave like synchronous code.

They are built on top of **Promises** and help avoid callback hell and complex `.then()` chains.

---

## 🔑 Key Concepts

| Keyword   | Description                                        |
|-----------|----------------------------------------------------|
| `async`   | Declares a function that returns a Promise         |
| `await`   | Pauses execution until the Promise is resolved     |

---

## 🧪 Declaring an Async Function

```js
async function greet() {
    return "Hello";
}

greet().then(msg => console.log(msg)); // Output: Hello
```

Even though `greet()` returns a string, it is automatically wrapped in a Promise.

---

## ⏳ Using `await` Inside `async`

```js
function fetchData() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("Data received");
        }, 2000);
    });
}

async function displayData() {
    const result = await fetchData(); // waits here until resolved
    console.log(result);
}

displayData(); // Output (after 2s): Data received
```

---

## 🚫 `await` Outside `async` ❌

```js
// ❌ This will throw a SyntaxError
const data = await fetchData();
```

`await` can only be used inside `async` functions (except in top-level `await` in ES modules or supported environments).

---

## 🛠 Error Handling with try...catch

```js
async function getUser() {
    try {
        const response = await fetch("https://api.example.com/user");
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Failed to fetch user:", error);
    }
}
```

---

## 🔁 Multiple Awaits (Sequential)

```js
async function loadAll() {
    const data1 = await fetchData1();
    const data2 = await fetchData2();
    console.log(data1, data2);
}
```

> Note: These run **sequentially**, which may be slower.

---

## 🏁 Run in Parallel with Promise.all()

```js
async function loadAllParallel() {
    const [data1, data2] = await Promise.all([fetchData1(), fetchData2()]);
    console.log(data1, data2);
}
```

> Better performance by running tasks concurrently.

---

## ✅ Summary

| Feature          | Benefit                                      |
|------------------|----------------------------------------------|
| `async` function | Returns a promise automatically              |
| `await` keyword  | Waits for the result of a Promise            |
| Cleaner syntax   | Avoids nested `.then()` and callbacks        |
| Easier debugging | Stack traces are simpler than with Promises  |

---

> ✨ Use `async/await` to write cleaner, more readable asynchronous JavaScript code — especially when working with APIs or long-running operations.

