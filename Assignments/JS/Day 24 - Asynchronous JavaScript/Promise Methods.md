# 🌐 JavaScript Promise Methods

JavaScript provides a set of static methods on the `Promise` object that allow developers to manage multiple asynchronous operations effectively. Here's a guide to all major Promise methods with examples.

---

## 1. `Promise.resolve(value)`

Returns a Promise that is **resolved** with the given value.

```js
const promise = Promise.resolve("Resolved!");
promise.then(console.log); // Output: Resolved!
```

## 2. `Promise.reject(error)`
Returns a Promise that is rejected with the given error.

```js
const promise = Promise.reject("Something went wrong");
promise.catch(console.error); // Output: Something went wrong
```

## 3. `Promise.all(iterable)`
Waits for all promises to resolve. If any promise is rejected, it immediately rejects.

```js
const p1 = Promise.resolve(1);
const p2 = Promise.resolve(2);
const p3 = Promise.resolve(3);

Promise.all([p1, p2, p3])
  .then(values => console.log(values)) // Output: [1, 2, 3]
  .catch(err => console.error(err));
```
> ⚠️ If any promise rejects, the entire `Promise.all()` rejects.

## 4. `Promise.allSettled(iterable)`
Waits for all promises to settle (resolve or reject). Returns an array of results.

```js
const p1 = Promise.resolve("✅ Success");
const p2 = Promise.reject("❌ Failure");

Promise.allSettled([p1, p2])
  .then(results => console.log(results));
```

```output
OUTPUT
[
  { status: "fulfilled", value: "✅ Success" },
  { status: "rejected", reason: "❌ Failure" }
]
```

## 5. `Promise.race(iterable)`
Returns a Promise that settles as soon as any one of the input promises settles (either resolves or rejects).

```js
const p1 = new Promise(resolve => setTimeout(resolve, 1000, "1s"));
const p2 = new Promise(resolve => setTimeout(resolve, 500, "0.5s"));

Promise.race([p1, p2]).then(console.log); // Output: 0.5s
```

## 6. `Promise.any(iterable)`
Returns a Promise that resolves as soon as any of the input promises resolves. If all are rejected, it rejects with an AggregateError.

```js
const p1 = Promise.reject("Error 1");
const p2 = Promise.resolve("First Success");
const p3 = Promise.resolve("Second Success");

Promise.any([p1, p2, p3])
  .then(console.log) // Output: First Success
  .catch(err => console.error(err));
```

> ⚠️ Unlike `race()`, `any()` ignores rejected promises until at least one is resolved.

## 7. `finally(callback)`
Runs a callback regardless of promise outcome (resolve or reject).
```js
fetchData()
  .then(data => console.log(data))
  .catch(error => console.error(error))
  .finally(() => console.log("Cleanup or final step"));
```

## 🧠 Summary Table
| Method                 | Purpose                                         |
| ---------------------- | ----------------------------------------------- |
| `Promise.resolve()`    | Creates a resolved promise                      |
| `Promise.reject()`     | Creates a rejected promise                      |
| `Promise.all()`        | Waits for all promises to resolve               |
| `Promise.allSettled()` | Waits for all promises to settle                |
| `Promise.race()`       | Resolves/rejects as soon as one promise settles |
| `Promise.any()`        | Resolves with the first fulfilled promise       |
| `.finally()`           | Executes callback after success/failure         |


## Conclusion
> 🔁 These methods allow for powerful control over async workflows, enabling better error handling, optimization, and readability.