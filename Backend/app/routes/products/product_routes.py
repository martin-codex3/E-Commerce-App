from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from ...schemas.products.product_schemas import CreateProductSchema, UpdateProductSchema
from ...services.products.product_service import ProductService
from ...connection.app_database_connection import get_app_session
from sqlmodel.ext.asyncio.session import AsyncSession


products_router = APIRouter()
product_service = ProductService()


# for fetching all the products here
@products_router.get("/", status_code=status.HTTP_200_OK)
async def index(session: AsyncSession = Depends(get_app_session)):
    all_products = await product_service.all_products(session = session)
    if all_products is not None:
        return all_products
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to fetch the records")


# for creating a new product here
@products_router.post("/", status_code=status.HTTP_200_OK)
async def store(product_data: CreateProductSchema, session: AsyncSession = Depends(get_app_session)):
    new_product = await product_service.create_product(
        product_data = product_data,
        session = session
    )

    if new_product is not None:
        return new_product
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="failed to create the product")


# getting a single record
@products_router.get("/{product_id}", status_code=status.HTTP_200_OK)
async def show(product_id: int, session: AsyncSession = Depends(get_app_session)):
    product = await product_service.show_product(product_id = product_id, session = session)
    if product is not None:
        return product
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to fetch product with that id")


# updating a product
@products_router.put("/{product_id}", status_code=status.HTTP_200_OK)
async def update(product_id: int, product_data: UpdateProductSchema, session: AsyncSession = Depends(get_app_session)):
    updated_product = await product_service.update_product(
        product_id = product_id,
        session = session,
        product_data = product_data
    )

    if updated_product is not None:
        return updated_product
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot update the product with that id")


# for deleting the product here
@products_router.delete("/{product_id}", status_code=status.HTTP_200_OK)
async def delete(product_id: int, session: AsyncSession = Depends(get_app_session)):
    product = await product_service.delete_product(product_id = product_id, session = session)
    if product.product_id != product_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to delete record with that id")
    elif product is None:
        return JSONResponse(content="Record deleted successfully")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to delete the product")
