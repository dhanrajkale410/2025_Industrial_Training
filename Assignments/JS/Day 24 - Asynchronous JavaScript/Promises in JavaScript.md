# 🟡 JavaScript Promises

A **Promise** in JavaScript represents the eventual **completion (or failure)** of an asynchronous operation and its resulting value.

It is a modern alternative to callbacks for managing asynchronous behavior and helps avoid "callback hell".

---

## 🔁 What is a Promise?

A Promise is an **object** that may be in one of 3 states:

| State      | Meaning                                       |
|------------|-----------------------------------------------|
| `pending`  | Initial state, neither fulfilled nor rejected |
| `fulfilled`| Operation completed successfully              |
| `rejected` | Operation failed                              |

---

## ✨ Creating a Promise

```js
const myPromise = new Promise((resolve, reject) => {
    let success = true;

    setTimeout(() => {
        if (success) {
            resolve("✅ Data fetched successfully");
        } else {
            reject("❌ Error while fetching data");
        }
    }, 2000);
});
```

## ✅ Consuming a Promise
You handle the result of a Promise using .then() for success and .catch() for errors:

```js
myPromise
    .then((result) => {
        console.log(result); // ✅ Data fetched successfully
    })
    .catch((error) => {
        console.error(error); // ❌ Error while fetching data
    });
```

## 🔄 Promise Chaining
You can chain .then() calls to perform a series of async tasks:

```js
doTask()
    .then(result => doNextTask(result))
    .then(nextResult => doFinalTask(nextResult))
    .catch(error => console.error("Something went wrong:", error));

```

## ⏱ Real-World Example

```js
function getUserData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve({ username: "dhanraj", age: 18 });
        }, 1000);
    });
}

getUserData()
    .then((user) => {
        console.log("User:", user);
    })
    .catch((err) => {
        console.error(err);
    });
```

## 🧠 Promise Summary

| Concept      | Description                    |
| ------------ | ------------------------------ |
| `resolve()`  | Call this to indicate success  |
| `reject()`   | Call this to indicate failure  |
| `.then()`    | Runs when Promise is fulfilled |
| `.catch()`   | Runs when Promise is rejected  |
| `.finally()` | Runs regardless of outcome     |

## 🚀 Bonus: Promise.all()
Run multiple Promises in parallel and wait for all to finish:
```js
Promise.all([promise1, promise2, promise3])
    .then(results => {
        console.log("All done:", results);
    })
    .catch(error => {
        console.error("At least one failed:", error);
    });
```

## Conclusion 
✅ Promises make your asynchronous code cleaner and more readable, especially when combined with async/await