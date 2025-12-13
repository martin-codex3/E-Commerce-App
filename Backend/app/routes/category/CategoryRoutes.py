from fastapi import APIRouter, HTTPException, status


category_router = APIRouter()


@category_router.get("/", status_code=status.HTTP_200_OK)
async def index():
    return {"message": "all categories will be fetched here"}