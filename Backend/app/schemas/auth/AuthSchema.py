from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

# for creating a new user
class SignUpUser(BaseModel):
    first_name: str = Field(default=None)
    last_name: str
    username: str
    email: EmailStr
    password: str = Field(exclude=True)
    created_at: datetime = Field(default=datetime.now())


# for logging in the user
class SignInUser(BaseModel):
    email: EmailStr
    password: str = Field(exclude=True)
