# Hoisting in JavaScript
> Hoisting is JavaScript's default behavior of moving declarations to the top of their scope before code execution.

## What Gets Hoisted?

| Declaration Type | Hoisted? | Initialized?                     |
| ---------------- | -------- | -------------------------------- |
| `var`            | ✅ Yes   | ❌ No (set to `undefined`)        |
| `let` / `const`  | ✅ Yes   | ❌ No (in **Temporal Dead Zone**) |
| `function`       | ✅ Yes   | ✅ Yes (whole function)           |
| `arrow function` | ❌ No    | ❌ No                             |

## Example with var (Hoisted)

```javascript
console.log(x); // undefined (not ReferenceError)
var x = 5;
```

> Internally becomes:

```javascript
var x;
console.log(x); // undefined
x = 5;
```

## Example with let/const (Hoisted but Not Accessible)

```javascript
console.log(y); // ❌ ReferenceError
let y = 10;
```

## Function Declaration (Hoisted)

```javascript
sayHello(); // ✅ Works

function sayHello() {
    console.log("Hello!");
}
```
## Function Expression (NOT Hoisted)

```javascript
sayHi(); // ❌ TypeError: sayHi is not a function

var sayHi = function () {
    console.log("Hi!");
};
```

## Temporal Dead Zone (TDZ)
Variables declared with let and const are hoisted, but cannot be accessed until the line where they are declared — this phase is known as the Temporal Dead Zone.

```javascript
console.log(a); // ❌ ReferenceError
let a = 10;
```

## Summary
- Hoisting moves declarations to the top, not initializations.
- var is hoisted and initialized as undefined.
- let/const are hoisted but in the TDZ, causing errors if accessed early.
- Function declarations are fully hoisted (you can call them early).
- Function expressions and arrow functions are not hoisted.