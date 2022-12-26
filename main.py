from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role, UserUpdateRequest

#/docs -> documentação interativa

app = FastAPI()

db: List[User] =  [
    User(
        id= UUID("f5b0004b-8d1f-41e8-8e74-9ebfa478f2f6"), 
        first_name="Cristina",
        last_name="Rodrigues",
        gender= Gender.female, 
        roles=[Role.student],
    ),
    User(
        id= UUID("d8ed56d2-557c-48d5-80ce-05c6b198ced5"), 
        first_name="Alexandre",
        last_name="Rodrigues",
        gender= Gender.male, 
        roles=[Role.student, Role.user]
    )
]

@app.get("/") # root route
async def root():
    return {"Hello": "Mundo"}

@app.get("/api/v1/users")
async def fetch_users():
    return db    

@app.post("/api/v1/users")
async def register_users(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, 
        detail=f"user with id: {user_id} does not exists"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user_update: UserUpdateRequest):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None: 
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404, 
        detail=f"user with id: {user_id} does not exists"
    )