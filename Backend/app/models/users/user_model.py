from sqlmodel import SQLModel, Field
from datetime import datetime

class UserModel(SQLModel, table = True):

    __tablename__ = "users"

    user_id: int = Field(primary_key=True, default=None)
    first_name: str = Field(index=True)
    last_name: str
    username: str
    email: str
    password: str = Field(exclude=True)
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(datetime.now())
    updated_at: datetime = Field(datetime.now())
