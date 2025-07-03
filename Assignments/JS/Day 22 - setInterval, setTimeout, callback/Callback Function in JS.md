# Callback Functions in JavaScript

A **callback** is a **function passed as an argument** to another function. It allows code to be executed **after** another function has finished running.

---

## Why Use Callbacks?

JavaScript is asynchronous and non-blocking. Callbacks help:
- Handle asynchronous tasks (e.g., loading files, fetching data).
- Run code in a specific sequence.
- Avoid deeply nested code using named callbacks.

---

## Basic Example

```javascript
function greet(name) {
    console.log("Hello, " + name);
}

function processUserInput(callback) {
    const name = "Dhanraj";
    callback(name);
}

processUserInput(greet);
```

> greet is passed as a callback to processUserInput and called with the user's name.

## Anonymous Callback

```javascript
function sayHi(callback) {
    callback();
}

sayHi(function() {
    console.log("Hi there!");
});
```

##  Summary
- A callback is a function passed into another function.

- Used for asynchronous operations, like API calls or timers.

- Can be named or anonymous.