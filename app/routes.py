from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models import ToDo
from app.database import get_db
from app.schemas import ToDoCreate, ToDoRead, ToDoUpdate

router = APIRouter()


@router.post("/add_todo/", response_model=ToDoRead)
def create_todo(todo: ToDoCreate, db: Session = Depends(get_db)):
    db_todo = ToDo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.get("/get_todos/", response_model=List[ToDoRead])
def read_todos(db: Session = Depends(get_db)):
    return db.query(ToDo).all()


@router.put("/update_todo/{todo_id}", response_model=ToDoRead)
def update_todo(todo_id: int, todo: ToDoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    update_data = todo.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.delete("/delete_todo/{todo_id}", response_model=dict)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(db_todo)
    db.commit()
    return {"message": f"Todo with ID {todo_id} deleted successfully"}
