from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.connection.app_database_connection import get_app_session
from app.services.products.product_service import ProductService


product_router = APIRouter()
product_service = ProductService()


@product_router.get("/", status_code=status.HTTP_200_OK)
async def index(session: AsyncSession = Depends(get_app_session)):
    all_products = await product_service.get_all_products(session = session)
    if all_products is not None:
        return all_products
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to fetch the records")


# getting a single record
@product_router.get("/{product_id}", status_code=status.HTTP_200_OK)
async def show(product_id: int, session: AsyncSession = Depends(get_app_session)):
    product = await product_service.show_single_product(
        session = session,
        product_id = product_id
    )

    if product is not None:
        return product
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to fetch record with that id")
