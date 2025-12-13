from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from app.services.products.ProductsService import ProductsService
from sqlalchemy.ext.asyncio.session import AsyncSession
from app.connection.db_connection import get_session
from app.schemas.products.ProductsSchema import CreateProductSchema, ProductsSchema


products_router = APIRouter()
# for the services here
product_services = ProductsService()

# the routes for the products here
@products_router.get("/")
async def index(session: AsyncSession = Depends(get_session)):
    all_products = await product_services.all_products(session)
    if all_products is not None:
        return all_products
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No available products on this route")


# for adding a new product
@products_router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductsSchema)
async def create_new_product(product_data: CreateProductSchema, session: AsyncSession = Depends(get_session)):
    new_product = await product_services.create_product(product_data = product_data, session = session)
    if new_product is not None:
        return HTMLResponse(
            content={
                "message": "product created successfully",
            },
            status_code=status.HTTP_201_CREATED
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Failed to create the product"
            }
        )
