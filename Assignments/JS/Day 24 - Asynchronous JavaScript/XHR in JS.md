
# 📡 XMLHttpRequest (XHR) in JavaScript

`XMLHttpRequest` (XHR) is a built-in JavaScript object used to send HTTP or HTTPS requests to a server and load the response data back into the script — without reloading the page.

Though modern developers prefer `fetch()`, XHR is still important to understand, especially for legacy browser support or understanding the evolution of AJAX.

---

## 🔄 Basic XHR Lifecycle

1. Create an `XMLHttpRequest` object.
2. Initialize it using `.open(method, URL)`.
3. Set up a callback using `.onload` or `.onreadystatechange`.
4. Send the request with `.send()`.

---

## 🧪 Simple GET Request (XHR)

```js
const xhr = new XMLHttpRequest();

xhr.open("GET", "https://jsonplaceholder.typicode.com/posts/1");

xhr.onload = function () {
    if (xhr.status === 200) {
        console.log("Response:", JSON.parse(xhr.responseText));
    } else {
        console.error("Error:", xhr.statusText);
    }
};

xhr.send();
```

---

## 📤 POST Request (XHR)

```js
const xhr = new XMLHttpRequest();
xhr.open("POST", "https://jsonplaceholder.typicode.com/posts");

xhr.setRequestHeader("Content-Type", "application/json");

xhr.onload = function () {
    if (xhr.status === 201) {
        console.log("Created:", JSON.parse(xhr.responseText));
    }
};

const data = JSON.stringify({
    title: "foo",
    body: "bar",
    userId: 1
});

xhr.send(data);
```

---

## 📶 XHR States (`readyState`)

| State | Value | Description                       |
|-------|-------|-----------------------------------|
| 0     | UNSENT | Request not initialized          |
| 1     | OPENED | Server connection established    |
| 2     | HEADERS_RECEIVED | Request received       |
| 3     | LOADING | Processing request              |
| 4     | DONE   | Request finished & response ready|

Example using `onreadystatechange`:

```js
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        console.log(JSON.parse(xhr.responseText));
    }
};
```

---

## ❗ Error Handling with XHR

```js
xhr.onerror = function () {
    console.error("Request failed.");
};
```

---

## 🛠 Useful XHR Methods and Properties

| Method / Property      | Description                                 |
|------------------------|---------------------------------------------|
| `.open(method, url)`   | Initializes the request                     |
| `.send([body])`        | Sends the request to the server             |
| `.setRequestHeader()`  | Sets headers like Content-Type              |
| `.responseText`        | Returns raw text response                   |
| `.status`              | HTTP response status code                   |
| `.readyState`          | Current state of the request                |

---

## ✅ Summary

- XHR is the original method for making AJAX requests.
- It provides control over the request and response cycle.
- Modern projects use `fetch()` or libraries like `Axios`, but XHR is still relevant in older codebases.

---

> 💡 Tip: Use `XMLHttpRequest` when you need **fine-grained control** or are working in legacy environments. Prefer `fetch()` for simpler, modern workflows.
