# Todo API

The Todo API allows users to interact with the to-do list.

## Endpoints

### `GET /get_todos/`

Returns the list of all to-dos.

#### Example Response

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

### `POST /add_todo/`

Creates a new to-do item.

#### Request Body

```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, and bread"
}
```

#### Example Response

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, and bread",
  "completed": false,
  "created_at": "2023-05-17T10:00:00"
}
```

### `PUT /update_todo/{todo_id}`

Updates an existing to-do item.

#### Request Body

```json
{
  "title": "Updated title",
  "description": "Updated description",
  "completed": true
}
```

#### Example Response

```json
{
  "id": 1,
  "title": "Updated title",
  "description": "Updated description",
  "completed": true,
  "created_at": "2023-05-17T10:00:00"
}
```

### `DELETE /delete_todo/{todo_id}`

Deletes a to-do item.

#### Example Response

```json
{
  "message": "Todo with ID 1 deleted successfully"
}
```
