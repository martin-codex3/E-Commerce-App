from pydantic import EmailStr, BaseModel, Field, validator
from datetime import datetime


class CreateUserSchema(BaseModel):
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    username: str = Field(min_length=1)
    email: EmailStr = Field(default=None)
    password: str = Field(min_length=5, max_length=20)
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(datetime.now())
    updated_at: datetime = Field(datetime.now())


# for updating the users
class UpdateUserSchema(BaseModel):

    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str = Field(exclude=True)
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(datetime.now())
    updated_at: datetime = Field(datetime.now())


# for logging in the user here
class SignInSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=5, max_length=20)