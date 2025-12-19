from fastapi import APIRouter, status, HTTPException
from pydantic import EmailStr
from sqlmodel.ext.asyncio.session import AsyncSession
from app.schemas.users.user_schema import CreateUserSchema
from app.services.auth.auth_service import AuthService


auth_router = APIRouter()
auth_services = AuthService()


@auth_router.get("/", status_code=status.HTTP_201_CREATED)
async def create_account(user_data: CreateUserSchema, session: AsyncSession):
    """ we first have to check the user here"""
    email: EmailStr = user_data.email
    user = await auth_services.check_if_user_exists(
        email = email,
        session = session
    )

    if user is not None:
        new_user = await auth_services.create_new_user(
            user_data = user_data,
            session = session
        )

        return new_user
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to create the user check your details and try again"
        )