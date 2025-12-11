from fastapi import APIRouter


# we will use the api router to group all the routes here
auth_router = APIRouter()

@auth_router.get("/")
async def create_user():
    return {"message": "We are creating the user"}