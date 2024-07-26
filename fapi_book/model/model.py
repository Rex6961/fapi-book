from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str

    # Example of using model data
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
