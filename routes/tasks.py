from unittest import result
from fastapi import APIRouter, Response, status
from config.db import conn
from models.tasks import tasks, deleted_tasks
from schemas.task import Task
from cryptography.fernet import Fernet
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from typing import List

task = APIRouter()

@task.post("/tasks", status_code=HTTP_201_CREATED, tags=["Task"])
def create_task(task: Task):
    new_task = {'user_id': task.user_id, 'title': task.title, 'description': task.description}
    result = conn.execute(tasks.insert().values(new_task))
    return 'Task created successfully', HTTP_201_CREATED

@task.get("/tasks", response_model=List[Task], tags=["Task"])
def get_all_tasks():
    return conn.execute(tasks.select()).fetchall()

@task.get("/task/{userid}", response_model=Task, tags=["Task"])
def get_task_by_userid(userid: str):
    return conn.execute(tasks.select().where(tasks.c.user_id == userid)).fetchall()

@task.put("/tasks/{id}/{userid}", response_model=Task, tags=["Task"])
def update_task(id: str, userid: str, task: Task):
    if conn.execute(tasks.select().where(tasks.c.id == id and tasks.c.user_id == userid)).first():
        conn.execute(tasks.update().values(title=task.title, description=task.description).where(tasks.c.id == id and tasks.c.user_id == userid))
        return conn.execute(tasks.select().where(tasks.c.id == id and tasks.c.user_id == userid)).first()