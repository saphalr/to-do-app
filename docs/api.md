# API Documentation

This document describes the API endpoints for the Todo application.

## Base URL

All API endpoints are relative to: `http://localhost:8000`

## API Endpoints

### Get All Todos

```http
GET /get_todos/
```

Retrieves a list of all todo items.

**Response Format:**

```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, and bread",
    "completed": false,
    "created_at": "2023-05-17T10:00:00"
  }
]
```

### Create Todo

```http
POST /add_todo/
```

Creates a new todo item.

**Request Body:**

```json
{
  "title": "Complete API documentation",
  "description": "Write detailed API docs for the Todo app"
}
```

**Response:** The created todo item.

### Update Todo

```http
PUT /update_todo/{todo_id}
```

Updates an existing todo item.

**Request Body:**

```json
{
  "title": "Updated title",
  "description": "Updated description",
  "completed": true
}
```

**Response:** The updated todo item.

### Delete Todo

```http
DELETE /delete_todo/{todo_id}
```

Deletes a todo item.

**Response:**

```json
{
  "message": "Todo with ID 1 deleted successfully"
}
```
