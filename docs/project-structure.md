# Project Structure

This document outlines the organization of the Todo application codebase.

## Directory Structure

```
todo-app/
├── app/
|   ├── core/
|       ├──config.py        # Application configuration
│   ├── main.py             # FastAPI application initialization
│   ├── database.py         # Database connection and session management
│   ├── models.py           # SQLAlchemy ORM models
│   ├── routes.py           # API endpoints
│   └── schemas.py          # Pydantic models for request/response
├── tests/                  # Test suite
│   └── test_main.py        # API tests
├── docs/                   # Documentation
│   ├── index.md            # Documentation home
│   ├── api.md              # API reference
│   └── ...                 # Other documentation files
├── .env                    # Environment variables (not in version control)
├── .gitignore              # Git ignore file
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker Compose services
├── requirements.txt        # Production dependencies
└── requirements-dev.txt    # Development dependencies
```

## Key Components

### Application (`app/`)

- **main.py**: Initializes the FastAPI application, includes routers, and defines startup events.
- **database.py**: Sets up the database connection, session, and Base class for ORM models.
- **models.py**: Defines SQLAlchemy ORM models for database tables.
- **routes.py**: Contains all API endpoint handlers.
- **schemas.py**: Pydantic models for request validation and response serialization.
- **core/config.py**: Application configuration using Pydantic settings.

### Tests (`tests/`)

- **test_main.py**: API integration tests using pytest and TestClient.
