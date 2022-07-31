from fastapi import FastAPI
from routes.user import user
from routes.tasks import task

app = FastAPI(
    title="FastAPI To-do-list",
    description="A simple to-do-list API",
    version="0.0.1",
    openapi_tags=[{
        "name": "User",
        "description": "User management"
    }
    , {
        "name": "Task",
        "description": "Task management"
    }]
)
app.include_router(user)
app.include_router(task)