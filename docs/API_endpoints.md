# 📌 API Endpoints Documentation

## **🔹 Authentication Routes**

### **1️⃣ User Signup**
**Endpoint:** `POST /auth/signup`
**Description:** Registers a new user.
**Request Body:**
```json
{
  "username": "testuser",
  "password": "securepassword"
}
```
**Response:**
```json
{
  "message": "User created successfully"
}
```

### **2️⃣ User Login**
**Endpoint:** `POST /auth/login`
**Description:** Logs in a user and returns a JWT token.
**Request Body:**
```json
{
  "username": "testuser",
  "password": "securepassword"
}
```
**Response:**
```json
{
  "access_token": "your-jwt-token"
}
```

## **🔹 Task Management Routes**

### **3️⃣ Create a Task**
**Endpoint:** `POST /api/tasks`
**Description:** Creates a new task for the logged-in user.
**Headers:**
```json
{
  "Authorization": "Bearer your-jwt-token"
}
```
**Request Body:**
```json
{
  "title": "Finish project",
  "description": "Complete the AI-powered task manager",
  "priority": "high"
}
```
**Response:**
```json
{
  "message": "Task created successfully",
  "task": { "id": 1, "title": "Finish project", "priority": "high" }
}
```

### **4️⃣ Get All Tasks**
**Endpoint:** `GET /api/tasks`
**Description:** Retrieves all tasks for the logged-in user.
**Headers:**
```json
{
  "Authorization": "Bearer your-jwt-token"
}
```
**Response:**
```json
[
  { "id": 1, "title": "Finish project", "priority": "high" },
  { "id": 2, "title": "Study Flask", "priority": "medium" }
]
```

### **5️⃣ Update a Task**
**Endpoint:** `PUT /api/tasks/{task_id}`
**Description:** Updates a task.
**Headers:**
```json
{
  "Authorization": "Bearer your-jwt-token"
}
```
**Request Body:**
```json
{
  "title": "Study Flask and React",
  "priority": "medium"
}
```
**Response:**
```json
{
  "message": "Task updated successfully"
}
```

### **6️⃣ Delete a Task**
**Endpoint:** `DELETE /api/tasks/{task_id}`
**Description:** Deletes a task.
**Headers:**
```json
{
  "Authorization": "Bearer your-jwt-token"
}
```
**Response:**
```json
{
  "message": "Task deleted successfully"
}
```

## **📌 Notes:**
- **All task-related endpoints require a valid JWT token.**
- **Use Postman or a frontend to test the API.**
- **Ensure `Authorization` header includes `Bearer your-jwt-token` for protected routes.**
