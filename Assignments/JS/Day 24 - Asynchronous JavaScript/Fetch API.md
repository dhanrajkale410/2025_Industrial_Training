# 🌐 JavaScript Fetch API

The **Fetch API** provides a modern, promise-based way to make HTTP requests in JavaScript. It's simpler and cleaner than the older `XMLHttpRequest`.

---

## 🚀 Basic Syntax

```js
fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## 🧪 Example: GET Request

```js
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## 📤 Example: POST Request

```js
fetch("https://jsonplaceholder.typicode.com/posts", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    title: "foo",
    body: "bar",
    userId: 1
  })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## 📄 Handling Other Response Types

### Text
```js
fetch("/example.txt")
  .then(response => response.text())
  .then(data => console.log(data));
```

### Blob (e.g., images)
```js
fetch("/image.png")
  .then(response => response.blob())
  .then(blob => {
    const imgURL = URL.createObjectURL(blob);
    document.querySelector("img").src = imgURL;
  });
```

---

## 🔐 Setting Headers

```js
fetch("https://api.example.com/data", {
  headers: {
    "Authorization": "Bearer YOUR_TOKEN",
    "Accept": "application/json"
  }
});
```

---

## ❗ Error Handling

Always use `.catch()` for network errors and manually check for HTTP status codes:

```js
fetch("https://api.example.com/data")
  .then(response => {
    if (!response.ok) {
      throw new Error("HTTP status " + response.status);
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error("Fetch error:", error));
```

---

## 🧠 Summary

| Feature           | Description                                     |
|-------------------|-------------------------------------------------|
| Built-in          | No need for libraries                          |
| Promise-based     | Cleaner async syntax                           |
| Easy to Use       | Straightforward syntax for common tasks        |
| Modern Replacement| Replaces `XMLHttpRequest`                      |

---

> ✅ Use the Fetch API for making network requests in modern JavaScript — it's clean, efficient, and works well with `async/await`.
