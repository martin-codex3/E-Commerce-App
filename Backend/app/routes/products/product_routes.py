from fastapi import APIRouter

product_router = APIRouter()

@product_router.get("/")
async def index():
    return {"message": "we will start here with the app"}
