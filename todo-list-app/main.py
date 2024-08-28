from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Path, Query

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
async def get_todos():
    results = [
 	 { "id": "todo-0", "name": "Eat", "completed": True },
 	 { "id": "todo-1","name": "Sleep", "completed": False },
 	 { "id": "todo-2", "name": "Repeat", "completed": False },
 	 { "id": "todo-3", "name": "Rest", "completed": True },
	]	

    return results


