from database import  Session
from models import Todos
from pydantic import BaseModel, Field
from starlette import status
from fastapi import APIRouter, Path, HTTPException

router = APIRouter()

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3)
    priority: int = Field(gt=0, lt=6)
    complete: bool

@router.get("/", status_code=status.HTTP_200_OK)
async def get_todos():
    db = Session()
    Todo_list = db.query(Todos).all()
    db.close()
    
    return Todo_list

@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo_by_id(todo_id: int = Path(gt=0)):
    db = Session()
    todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo is not None:
        return todo
        db.close()
    raise HTTPException(status_code=404, detail="Todo not found")

@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(todo_request: TodoRequest):
    db = Session()
    todo = Todos(**todo_request.model_dump())
    db.add(todo)
    db.commit()
    db.close()
    
@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(todo_request: TodoRequest, todo_id: int = Path(gt=0)):
    db = Session()
    todo = db.query(Todos).filter(Todos.id == todo_id).first()
    
    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found.")
    
    todo.title = todo_request.title
    todo.description = todo_request.desription
    todo.priority = todo_request.priority
    todo.complete = todo_request.complete
    db.add(todo)
    db.commit()
    db.close()

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int = Path(gt=0)):
    db = Session()
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    
    if todo_model is None:
        raise HTTPException(status_code=404, detail="todo not found.")
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
