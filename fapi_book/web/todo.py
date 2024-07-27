from pathlib import Path as Pathlib

from fastapi import (
    APIRouter, Path, 
    HTTPException, status, 
    Request, Depends
    )
from fastapi.templating import Jinja2Templates

from ..model.model import Todo, TodoItem

top = Pathlib(__file__).resolve().parents[1]

todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory=f"{top}/templates/")

# This method creates variable
@todo_router.post("/todo", status_code=201)
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)) -> dict:
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html",
                                    {
                                        "request": request,
                                        "todos": todo_list
                                    })

# This method get all variables into TodoItem
@todo_router.get("/todo")
async def retrieve_todo(request: Request) -> dict:
    return templates.TemplateResponse("todo.html",
                                    {
                                        "request": request,
                                        "todos": todo_list
                                    })

# This method gets one variable
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("todo.html",
                            {
                                "request": request,
                                "todo": todo
                            })
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )
    
# This method updates todo_list variables
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int =
                      Path(..., title="The ID of the todo to be updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo update successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )

# This method deletes one variable
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo  with supplied ID doesn't exist",
    )

# This method deletes all variables
@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos deleted successfully."
    }
