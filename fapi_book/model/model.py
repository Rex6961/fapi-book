from pydantic import BaseModel
from fastapi import Form


class Todo(BaseModel):
    id: int = None
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)

    # Example of using model
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "item": "Example schema!"
                }
            ]
        }
    }

class TodoItem(BaseModel):
    item: str

    # Example of using model
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "item": "Read the next chapter of the book"
                }
            ]
        }
    }

class TodoItems(BaseModel):
    todos: list[TodoItem]

    # Example of using model
    model_config = {
        "json_schema_extra": {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }
    }
