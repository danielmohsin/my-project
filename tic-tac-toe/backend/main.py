from fastapi import FastAPI
import time  # Import the time module
from .api import endpoints

app = FastAPI()

@app.get("/")
def read_root():
    unix_time = int(time.time())  # Get the current Unix time
    return {"unix_time": unix_time}  # Return the Unix time

app.include_router(endpoints.router)

