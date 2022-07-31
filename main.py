from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="FastAPI To-do-list",
    description="A simple to-do-list API",
    version="0.0.1",
    openapi_tags=[{
        "name": "User",
        "description": "User management"
    }]
)
app.include_router(user)