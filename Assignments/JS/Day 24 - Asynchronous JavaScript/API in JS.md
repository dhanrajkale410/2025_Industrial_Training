
# 🌐 What is an API?

**API** stands for **Application Programming Interface**. It is a set of rules and definitions that allows one software application to communicate with another.

APIs allow developers to interact with external services, databases, or systems without needing to know their internal implementation.

---

## 🔑 Key Concepts

| Term         | Description                                           |
|--------------|-------------------------------------------------------|
| API          | A contract that defines how to interact with a system|
| Endpoint     | A specific URL where an API resource can be accessed |
| Request      | The call made to the API (GET, POST, etc.)           |
| Response     | The data returned by the API                         |
| JSON         | Common format for exchanging API data                |

---

## 📬 How APIs Work

1. Client sends a **request** to an API endpoint.
2. Server processes the request.
3. Server sends a **response** back to the client.

---

## 🌍 Example: Public REST API

### Request:
```http
GET https://jsonplaceholder.typicode.com/posts/1
```

### Response:
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat",
  "body": "quia et suscipit suscipit recusandae..."
}
```

---

## 🔄 HTTP Methods in REST APIs

| Method | Description                      |
|--------|----------------------------------|
| GET    | Retrieve data                    |
| POST   | Send new data                    |
| PUT    | Update existing data             |
| DELETE | Remove data                      |

---

## 🧰 Using APIs in JavaScript (with Fetch)

```js
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## 🔐 API Authentication (Example)

Some APIs require API keys or tokens.

```http
GET /user HTTP/1.1
Host: api.example.com
Authorization: Bearer YOUR_API_TOKEN
```

---

## 📦 Types of APIs

| Type            | Description                                        |
|------------------|----------------------------------------------------|
| REST             | Web-based, uses HTTP methods                       |
| SOAP             | Protocol-based, XML-based web services             |
| GraphQL          | Query language for APIs                            |
| Web APIs         | APIs provided by browsers (e.g., DOM, Fetch)       |
| Third-party APIs | Provided by services like Twitter, Google, etc.    |

---

## ✅ Summary

- APIs enable communication between different software systems.
- REST APIs use HTTP methods to access resources.
- APIs are used in web apps, mobile apps, IoT devices, and more.

---

> 💡 Learning how to work with APIs is essential for front-end and back-end developers alike.
