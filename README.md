# FastAPI Todo App

A simple RESTful API for managing to-do items built with FastAPI.

## Features

- Create, read, update, and delete to-do items
- Persistent storage with PostgreSQL (production) or SQLite (development)
- API documentation with FastAPI's built-in Swagger UI
- Containerized with Docker
- Comprehensive tests

## Technology Stack

- **FastAPI**: High-performance web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **PostgreSQL**: Production database
- **Pydantic**: Data validation and settings management
- **Docker**: Containerization
- **MkDocs**: Documentation generator

## Prerequisites

- Python 3.8+
- Docker and Docker Compose (for containerized setup)
- PostgreSQL (for production deployment)

## Getting Started

### Local Development Setup

1. **Clone the repository**

```bash
git clone https://github.com/saphalr/to-do-app.git
cd to-do-app
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file**

```
# Database
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_NAME=todos
DB_HOST=db
DB_PORT=5432

# Application
ENVIRONMENT=development
DEBUG=true
HOST=0.0.0.0
PORT=8000
```

5. **Run the application**

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000 and the interactive documentation at http://localhost:8000/docs

### Docker Setup

1. **Clone the repository**

```bash
git clone https://github.com/saphalr/to-do-app.git
cd to-do-app
```

2. **Create a `.env` file** (same as above)

3. **Start the containers**

```bash
docker-compose up -d
```

This will start:

- PostgreSQL database on port 5432
- API service on port 8000
- Documentation site on port 9000


## API Documentation

Once the application is running:

- Interactive API documentation (Swagger UI): http://localhost:8000/docs

With Docker, you can also access the MkDocs documentation at http://localhost:9000
Or you can run it manually using
```bash
mkdocs build
mkdocs serve -a 0.0.0.0:9000
```

### Main Endpoints

- `GET /get_todos/` - List all todos
- `POST /add_todo/` - Create a new todo
- `PUT /update_todo/{todo_id}` - Update a todo
- `DELETE /delete_todo/{todo_id}` - Delete a todo

## Running Tests

```bash
# Run tests
pytest

```
