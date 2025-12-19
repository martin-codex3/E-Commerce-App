from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.users.user_model import UserModel
from sqlmodel import select
from pydantic import EmailStr
from app.schemas.users.user_schema import CreateUserSchema


class AuthService:

    """this function will attempt to fetch the user by their email"""
    async def get_user_by_email(self, email: EmailStr, session: AsyncSession):
        """we have to fetch the user by the provided email here"""
        statement = select(UserModel).where(UserModel.email == email)
        results = await session.exec(statement)

        user = results.first()
        return user


    """this function will check if the user exists in the database here"""
    async def check_if_user_exists(self, email: EmailStr, session: AsyncSession):
        user = await self.get_user_by_email(email = email, session = session)

        if user is not None:
            return True
        else:
            return False


    """ the function will attempt to create the new user"""
    async def create_new_user(self, user_data: Create):