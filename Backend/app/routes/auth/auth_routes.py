from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import EmailStr
from sqlmodel.ext.asyncio.session import AsyncSession
from app.schemas.users.user_schema import CreateUserSchema
from app.services.auth.auth_service import AuthService
from app.connection.app_database_connection import get_app_session


auth_router = APIRouter()

auth_services = AuthService()


@auth_router.post("/create-account", status_code=status.HTTP_201_CREATED)
async def create_account(user_data: CreateUserSchema, session: AsyncSession = Depends(get_app_session)):
    """ we first have to check the user here"""
    email: EmailStr = user_data.email

    # checking if the user exists
    user_exists = await auth_services.check_if_user_exists(email = email, session = session)

    if user_exists:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail="Email address already taken, try another email")

    else:
        new_user = await auth_services.create_new_user(
            user_data = user_data,
            session = session
        )

        return new_user
