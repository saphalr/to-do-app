from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import ToDo
from app.database import get_db
from app.schemas import ToDoCreate, ToDoRead

router = APIRouter()


@router.post("/add_todo/", response_model=ToDoRead)
def create_todo(todo: ToDoCreate, db: Session = Depends(get_db)):
    db_todo = ToDo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.get("/get_todos/", response_model=list[ToDoRead])
def read_todos(db: Session = Depends(get_db)):
    return db.query(ToDo).all()
