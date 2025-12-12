from sqlmodel import Field, SQLModel
from pydantic import EmailStr
from datetime import datetime


class User(SQLModel, table=True):
    __tablename__ = "users"

    user_id: int = Field(default=None, primary_key=True)
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    username: str = Field(index=True)
    email: EmailStr = Field(index=True, unique=True)
    password: str
    created_at: datetime = Field(default=datetime.now())
