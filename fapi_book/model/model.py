from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str

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

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "item": "Read the next chapter of the book"
                }
            ]
        }
    }
