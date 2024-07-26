from fastapi import APIRouter, Path

from ..model.model import Todo, TodoItem


todo_router = APIRouter()

todo_list = []

# This method creates variable
@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}

# This method gets all variables
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}

# This method gets one variable
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
        return {
            "message": "Todo with supplied ID doesn't exist."
        }
    
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
        return {
            "message": "Todo with supplied ID doesn't exist."
        }

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
        return {
            "message": "Todo with supplied ID doesn't exist."
        }

# This method deletes all variables
@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos deleted successfully."
    }
