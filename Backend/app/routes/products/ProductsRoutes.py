from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from app.services.products.ProductsService import ProductsService
from sqlalchemy.ext.asyncio.session import AsyncSession
from app.connection.db_connection import get_session
from app.schemas.products.ProductsSchema import CreateProductSchema, ProductsSchema, UpdateProductSchema
from typing import List

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
@products_router.post("/", status_code=status.HTTP_201_CREATED)
async def store(product_data: CreateProductSchema, session: AsyncSession = Depends(get_session)):
    new_product = await product_services.create_product(product_data = product_data, session = session)
    if new_product is not None:
        return new_product
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Failed to create the product"
            }
        )


# for getting a single record here
@products_router.get("/{product_id}", status_code=status.HTTP_200_OK)
async def show(product_id: int, session: AsyncSession = Depends(get_session)):
    product = await product_services.show_product(product_id = product_id, session = session)
    if product is not None:
        return product
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to fetch a record with the id")


# updating the product here
@products_router.put("/{product_id}", status_code=status.HTTP_200_OK)
async def update(product_id: int, product_data: UpdateProductSchema, session: AsyncSession = Depends(get_session)):
    product = await product_services.update_product(
        product_id = product_id,
        session = session,
        product_data = product_data
    )

    if product is not None:
        return product
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to update the product"
        )


# we will attempt to delete the data here
@products_router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(product_id: int, session: AsyncSession = Depends(get_session)):
    product = await product_services.delete_product(
        product_id = product_id,
        session = session
    )

    if product is None:
        return HTMLResponse(
            content="Record deleted successfully"
        )
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to delete the table with that id")
