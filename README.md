# GraphQL API with Flask and Graphene

## 📖 Introduction

This project demonstrates how to build a simple GraphQL API using Flask and Graphene. GraphQL is a modern query language that allows clients to request only the data they need, making it more efficient than traditional REST APIs. We also use the **Altair GraphQL Client** to test our queries, providing an easy-to-use interface for interacting with the API.

---

## ✨ Features

- **Dynamic Queries**: Fetch specific data using GraphQL.
- **Custom Resolvers**: Define how data is retrieved for each field in the schema.
- **Altair Integration**: Use the Altair GraphQL Client for testing queries effortlessly.

---

## ⚙️ How It Works

### 1. Schema Definition
The schema defines what data the API can provide. Fields like `hello` are defined, along with how they resolve their data.

### 2. Flask Setup
A Flask server hosts the GraphQL API. The `/graphql` endpoint listens for incoming POST requests containing GraphQL queries.

### 3. Query Execution
When a query is sent to the API, the server:
- Validates the request.
- Executes the query using the schema.
- Returns the response, including the requested data or any errors.

### 4. Error Handling
The server checks for errors during query execution and ensures meaningful error messages are returned.

### 5. Testing with Altair
Altair is used to send queries to the `/graphql` endpoint, making it easy to explore and test the API.

---

## 🚀 How to Run the Project

1. **Install Dependencies**:
   - Install Flask and Graphene using `pip`.

2. **Start the Server**:
   - Run the Flask application on `http://127.0.0.1:5000`.

3. **Test with Altair**:
   - Download and open the [Altair GraphQL Client](https://altair.sirmuel.design/).
   - Set the endpoint to `http://127.0.0.1:5000/graphql`.
   - Send queries like:
     ```graphql
     {
       hello
     }
     ```

---

## 🛠 Why Use This Setup?

- **Flexibility**: GraphQL allows clients to request only the data they need, making it highly efficient.
- **Ease of Testing**: Altair provides a clean interface for quickly sending and testing queries.
- **Scalability**: This basic setup can be extended with complex schemas, mutations, and database integrations.

---

## ⚠️ Limitations

- **Error Handling**: Advanced error handling is not included in this basic setup.
- **No Authentication**: Sensitive data queries require authentication and authorization layers.

---

## 🏁 Conclusion

This project provides a lightweight introduction to building GraphQL APIs using Flask and Graphene. Combined with the Altair GraphQL Client, it offers a simple yet powerful way to learn and test GraphQL capabilities. Expand on this by adding mutations, more complex fields, or database connections to build robust, real-world APIs.