from sqlmodel import SQLModel, Field
from datetime import datetime

class UserModel(SQLModel, table=True):

    __tablename__ = "user"

    user_id: int = Field(default=None, primary_key=True)
    first_name: str = Field(default=None, index=True)
    last_name: str = Field(default=None, index=True)
    username: str = Field(default=None, index=True)
    email: str = Field(default=None)
    password: str = Field(exclude=True)
    is_active: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.date)
