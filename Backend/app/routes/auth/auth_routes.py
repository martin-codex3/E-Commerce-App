from fastapi import APIRouter, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from app.schemas.users.user_schema import CreateUserSchema
from app.services.auth.auth_service import AuthService


auth_router = APIRouter()
auth_services = AuthService()


@auth_router.get("/", status_code=status.HTTP_201_CREATED)
async def create_account(user_data: CreateUserSchema, session: AsyncSession):
    """ we first have to check the user here"""
