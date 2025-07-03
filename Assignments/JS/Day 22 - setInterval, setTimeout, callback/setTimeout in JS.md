# `setTimeout()` in JavaScript

`setTimeout()` is a built-in JavaScript method used to execute a function **once after a specified delay** (in milliseconds).

## Syntax

```javascript
setTimeout(function, delay, param1, param2, ...)
```
- function: The function to execute.
- delay: The time to wait (in milliseconds) before executing the function.
- param1, param2, ...: Optional parameters to pass to the function.

## Basic Example

```javascript
setTimeout(() => {
    console.log("This message appears after 2 seconds");
}, 2000);
```

## Using a Named Function

```javascript
function greet() {
    console.log("Hello, world!");
}

setTimeout(greet, 1000); // Executes greet() after 1 second
```

## Passing Arguments

```javascript
function sayHello(name) {
    console.log("Hello, " + name);
}

setTimeout(sayHello, 1500, "Dhanraj");
```

## Cancelling setTimeout
Use clearTimeout() to cancel a scheduled timeout.

```javascript
const timeoutId = setTimeout(() => {
    console.log("You won't see this message");
}, 3000);

clearTimeout(timeoutId);
```

## Use Cases
- Delaying function execution
- Showing splash screens or tooltips
- Scheduling retries
- Creating fake loading animations

## Difference from setInterval

| Method        | Repeats Execution? | Can Be Cancelled? |
| ------------- | ------------------ | ----------------- |
| `setTimeout`  | ❌ No              | ✅ Yes           |
| `setInterval` | ✅ Yes             | ✅ Yes           |

## Summary
- setTimeout() runs code once after a delay.
- Can be cancelled using clearTimeout().
- Useful for creating delays, timeouts, or simulating asynchronous behavior.

> Combine setTimeout() with callbacks or promises for better async control.