from fastapi import APIRouter, HTTPException, Response
from conf.db import conn
from models.user import User as UserModel
from schemas.user import User as UserSchema
from cryptography.fernet import Fernet
from starlette import status
from datetime import datetime

user = APIRouter()
key = Fernet.generate_key()
keygen = Fernet(key)


@user.get("/users", response_model=list[UserSchema], tags=["User"])
def get_users():
    return conn.execute(UserModel.select()).fetchall()


@user.get("/users/{id}", response_model=UserSchema, tags=["User"])
def get_user(user_id: int):
    return conn.execute(UserModel.select().where(UserModel.c.id == user_id)).fetchone()


@user.post("/users", response_model=UserSchema, tags=["User"])
def create_user(user: UserSchema):
    new_user = {"name": user.name, "email": user.email, "password": keygen.encrypt(user.password.encode("utf-8")),
                "created_at": datetime.now(), "updated_at": datetime.now()}
    result = conn.execute(UserModel.insert().values(new_user))
    return conn.execute(UserModel.select().where(UserModel.c.id == result.lastrowid)).fetchone()


@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["User"])
def delete_user(user_id: int):
    result = conn.execute(UserModel.delete().where(UserModel.c.id == user_id))
    if result.rowcount == 0:
        return HTTPException(status_code=404, detail=f"user {user_id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@user.put("/users/{id}", response_model=UserSchema, tags=["User"])
def update_user(user_id: int, user: UserSchema):
    result = conn.execute(UserModel.update().values(name=user.name,
                                                    email=user.email,
                                                    password=keygen.encrypt(user.password.encode("utf-8")),
                                                    updated_at=datetime.now()).where(UserModel.c.id == user_id))
    if result.rowcount == 0:
        return HTTPException(status_code=404, detail=f"user {user_id} not found")
    return conn.execute(UserModel.select().where(UserModel.c.id == user_id)).fetchone()

