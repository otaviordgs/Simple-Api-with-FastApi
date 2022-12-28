from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserBase):
    db_user = models.User(
        first_name = user.first_name,
        last_name = user.last_name,
        age = user.age
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_update: schemas.UserUpdate, user_id: int):
    user: schemas.User = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail=f"User not found with id {user_id}")
    if user_update.first_name is not None:
        user.first_name = user_update.first_name
    if user_update.last_name is not None:
        user.last_name = user_update.last_name
    if user_update.age is not None:
        user.age = user_update.age
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

