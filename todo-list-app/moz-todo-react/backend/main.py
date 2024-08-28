from fastapi import FastAPI, HTTPException
from sqlalchemy import select
from fastapi.middleware.cors import CORSMiddleware

from .database import DatabaseSession, engine
from .models import Base, Todo
from .schemas import CreateTodo, UpdateTodo

# Initialize the DB tables if they don't exist
Base.metadata.create_all(engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/todos")
def list_todos(session: DatabaseSession):
    return session.scalars(select(Todo)).all()

@app.post("/todos")
def create_todo(body: CreateTodo, session: DatabaseSession):
    todo = Todo(name=body.name)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@app.patch("/todos/{id}")
def update_todo(id: int, body: UpdateTodo, session: DatabaseSession):
    todo = session.get(Todo, id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    if body.name is not None:
        todo.name = body.name
    if body.completed is not None:
        todo.completed = body.completed
    session.commit()
    session.refresh(todo)
    return todo

@app.delete("/todos/{id}")
def delete_todo(id: int, session: DatabaseSession):
    todo = session.get(Todo, id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    session.delete(todo)
    session.commit()

