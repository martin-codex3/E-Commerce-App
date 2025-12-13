from fastapi import APIRouter


products_router = APIRouter()

# the routes for the products here
@products_router.get("/")
async def index():
    return {"message": "we will start here with the app"}
