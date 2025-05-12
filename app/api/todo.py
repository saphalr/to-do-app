from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_todo():
    return {"message": "This is the to-do route"}
