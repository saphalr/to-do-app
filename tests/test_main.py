from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from app.main import app
from app.database import get_db, Base

# Create SQLite in-memory database for testing
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"
test_engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


# Override the dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


@pytest.fixture(scope="function")
def setup_db():
    # Create tables
    Base.metadata.create_all(bind=test_engine)
    yield
    # Drop tables after test
    Base.metadata.drop_all(bind=test_engine)


def test_crud_operations(setup_db):
    # Test create todo
    create_response = client.post(
        "/add_todo/",
        json={"title": "Test Todo", "description": "This is a test todo"},
    )
    assert create_response.status_code == 200
    created_todo = create_response.json()
    assert created_todo["title"] == "Test Todo"
    assert created_todo["description"] == "This is a test todo"
    assert created_todo["completed"] is False
    todo_id = created_todo["id"]

    # Test read todos
    read_response = client.get("/get_todos/")
    assert read_response.status_code == 200
    todos = read_response.json()
    assert len(todos) == 1
    assert todos[0]["id"] == todo_id

    # Test update todo
    update_response = client.put(
        f"/update_todo/{todo_id}",
        json={"title": "Updated Todo", "completed": True},
    )
    assert update_response.status_code == 200
    updated_todo = update_response.json()
    assert updated_todo["title"] == "Updated Todo"
    assert updated_todo["completed"] is True
    assert updated_todo["description"] == "This is a test todo"  # unchanged

    # Test delete todo
    delete_response = client.delete(f"/delete_todo/{todo_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == (
        f"Todo with ID {todo_id} deleted successfully"
    )

    # Verify todo is deleted
    read_after_delete = client.get("/get_todos/")
    assert len(read_after_delete.json()) == 0


def test_update_nonexistent_todo(setup_db):
    response = client.put(
        "/update_todo/999",
        json={"title": "This should fail"},
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"


def test_delete_nonexistent_todo(setup_db):
    response = client.delete("/delete_todo/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"
