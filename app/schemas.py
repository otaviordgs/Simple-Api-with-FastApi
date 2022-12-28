from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    first_name: str
    last_name: str
    age: int


class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

