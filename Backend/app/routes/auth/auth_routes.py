from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import EmailStr
from sqlmodel.ext.asyncio.session import AsyncSession
from app.schemas.users.user_schema import CreateUserSchema, SignInSchema
from app.services.auth.auth_service import AuthService
from app.connection.app_database_connection import get_app_session
from app.utils.jwt_password_management import create_jwt_token
from app.utils.password_management import verify_password
from datetime import timedelta


auth_router = APIRouter()
auth_services = AuthService()


@auth_router.post("/create-account", status_code=status.HTTP_201_CREATED)
async def create_account(user_data: CreateUserSchema, session: AsyncSession = Depends(get_app_session)):
    """ we first have to check the user here"""
    email: EmailStr = user_data.email

    # checking if the user exists
    user_exists = await auth_services.check_if_user_exists(email = email, session = session)

    if user_exists:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail={
            "message": "Email address already taken, try another email"
        })

    else:
        user = await auth_services.create_new_user(
            user_data = user_data,
            session = session
        )

        return JSONResponse(
            content={
                "message": "Account created successfully",
                "user": {
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    "created_at": str(user.created_at),
                    "updated_at": str(user.updated_at)
                },
            },
            status_code=status.HTTP_201_CREATED
        )


# the route for logging the users in
@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(user_data: SignInSchema, session: AsyncSession = Depends(get_app_session)):
    email = user_data.email
    password = user_data.password

    user = await auth_services.get_user_by_email(
        email = email,
        session = session
    )

    # we have to check if the use is available here
    if user is not None:
        password_valid = verify_password(password, user.password)
        # we have to check if the password is valid here
        if password_valid:
            access_token = create_jwt_token(
                user_data = {
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                },
                refresh = False
            )

            # we have to also create the refresh token here
            refresh_token = create_jwt_token(
                user_data = {
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    "created_at": str(user.created_at),
                    "updated_at": str(user.updated_at)
                },
                refresh = True,
                expiry=timedelta(days=7)
            )

            # we have to return the json response here
            return JSONResponse(
                content={
                    "message": "Logged in successfully",
                    "user": {
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "username": user.username,
                    },
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                }
            )
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Password")

    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Email or Password")
