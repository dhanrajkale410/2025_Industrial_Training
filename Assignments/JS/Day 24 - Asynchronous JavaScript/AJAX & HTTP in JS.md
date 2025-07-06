# 🌐 Introduction to AJAX and HTTP Requests

AJAX stands for **Asynchronous JavaScript and XML**. It allows web pages to send and receive data from a server asynchronously **without reloading the entire page**.

---

## ⚙️ What is AJAX?

AJAX enables:
- Updating parts of a web page without reloading.
- Making background HTTP requests.
- Receiving data in formats like JSON, XML, HTML, or plain text.

### Example Use Cases:
- Submitting forms without page refresh.
- Live search suggestions.
- Dynamic content loading (e.g., infinite scroll).

---

## 🌍 HTTP Requests Overview

AJAX communicates with servers using **HTTP methods**:

| Method | Description                         |
|--------|-------------------------------------|
| GET    | Retrieve data from the server       |
| POST   | Send data to the server             |
| PUT    | Update existing data                |
| DELETE | Remove data                         |

---

## 🔧 Making an AJAX Request

### 1. Using `XMLHttpRequest` (Old Way)

```js
const xhr = new XMLHttpRequest();
xhr.open("GET", "https://api.example.com/data");
xhr.onload = function () {
    if (xhr.status === 200) {
        console.log(JSON.parse(xhr.responseText));
    } else {
        console.error("Error fetching data");
    }
};
xhr.send();
```
---
### 2. Using fetch() (Modern Way)

```js
fetch("https://api.example.com/data")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error("Error:", error));
```
---
### 3. Using async/await (With fetch)
```js
async function getData() {
    try {
        const response = await fetch("https://api.example.com/data");
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error:", error);
    }
}
getData();
```
---

## 📥 Sending Data with POST

```js
fetch("https://api.example.com/submit", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ name: "John", age: 25 })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));
```
---
## 🧠 Key Concepts
| Term         | Meaning                                                 |
| ------------ | ------------------------------------------------------- |
| AJAX         | Asynchronous server communication without reloading     |
| HTTP Methods | Actions to perform on server resources (GET, POST, etc) |
| fetch()      | Modern API for making HTTP requests                     |
| JSON         | Common data format for AJAX responses                   |
---

## ✅ Summary
- AJAX allows background communication with servers.

- HTTP methods define what kind of data operation is performed.

- Use modern fetch() or async/await for clean and readable code.

- Enables smoother and more interactive web applications.

> 🔁 AJAX is a key part of modern web development for creating dynamic, real-time user experiences.