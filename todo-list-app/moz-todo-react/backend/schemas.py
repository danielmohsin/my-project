# schemas.py
from pydantic import BaseModel


class CreateTodo(BaseModel):
    name: str


class UpdateTodo(BaseModel):
    name: str | None = None
    completed: bool | None = None

