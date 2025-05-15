# FastAPI Todo App Documentation

Welcome to the documentation for the FastAPI Todo App - a simple yet powerful task management API.

## Overview

This application provides a RESTful API for managing to-do tasks with the following features:

- Create, read, update, and delete to-do items
- Task status tracking with completion states
- SQLAlchemy ORM for database interactions
- Pydantic for data validation


## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to use the interactive API documentation.
