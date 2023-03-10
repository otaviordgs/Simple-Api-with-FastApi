from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal

#/docs -> documentação interativa
# run -> uvicorn main:app --reload
# __init__.py serve para reconhecer a pasta como modulo e assim podemos fazer import dela


app = FastAPI()
# respionsavel por criar a tabela no banco de dados
models.Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/") # root route
async def root():
    return {"Hello": "World"}

@app.get("/users/{user_id}", response_model=schemas.User)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db=db,user_id=user_id)
    return user

@app.get("/users", response_model=List[schemas.User])
async def fetch_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users    

@app.post("/users", response_model=schemas.User)
async def register_users(user: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.delete("/users")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db=db, user_id=user_id)

@app.put("/users/{user_id}", response_model=schemas.User)
async def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_update=user_update, user_id=user_id)
