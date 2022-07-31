from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User
user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def create_users(user: User):
    new_user = {'name': user.name, 'email': user.email, 'password': user.password}
    return {"users": "users"}

@user.get("/users")
def get_users():
    return {"users": "users"}

@user.get("/users")
def get_users():
    return {"users": "users"}

@user.get("/users")
def get_users():
    return {"users": "users"}