# Callbacks in Asynchronous Programming

In JavaScript, **callbacks** are functions passed as arguments to other functions, which are **executed later**, often after an asynchronous operation completes. They are one of the earliest and most common patterns used to handle **asynchronous behavior**.

---

## 🔁 What is a Callback?

A **callback function** is:
- Passed as an argument to another function.
- Executed after the completion of that function.

```js
function fetchData(callback) {
    setTimeout(() => {
        console.log("Data fetched!");
        callback();
    }, 2000); // simulates a delay
}

function processData() {
    console.log("Processing data...");
}

fetchData(processData);
```

---

## 📦 Why Use Callbacks?
JavaScript is non-blocking. While waiting for operations like:

- API calls

- File reads

- Timers

...you can continue execution using callbacks when the operation completes.

---

## ⚠️ Callback Hell
Nested callbacks can lead to hard-to-read and hard-to-maintain code, often referred to as callback hell.

```js
doSomething(function(result) {
    doSomethingElse(result, function(newResult) {
        doThirdThing(newResult, function(finalResult) {
            console.log('Final result:', finalResult);
        });
    });
});
```

This deep nesting is difficult to manage and debug.

## ✅ Solutions to Callback Hell
To solve these issues, modern JavaScript introduced:

- Promises

- Async/Await (syntax sugar over promises)

- These provide cleaner and more manageable ways to handle asynchronous code.


## 🧠 Summary

| Feature             | Description                                 |
| ------------------- | ------------------------------------------- |
| What                | A function passed to another function       |
| When                | Executes after an async operation completes |
| Use Case            | Network requests, file I/O, timers          |
| Problem             | Callback Hell (deeply nested functions)     |
| Modern Alternatives | Promises, Async/Await                       |


> 📝 Tip: Always handle errors inside callbacks using proper error handling techniques.

```js
function fetchData(callback) {
    setTimeout(() => {
        const error = false;
        if (error) {
            callback("Something went wrong!", null);
        } else {
            callback(null, "Data fetched!");
        }
    }, 1000);
}

fetchData((err, data) => {
    if (err) {
        console.error(err);
    } else {
        console.log(data);
    }
});
```