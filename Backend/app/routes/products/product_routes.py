from os import access

from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.connection.app_database_connection import get_app_session
from app.schemas.products.product_schemas import UpdateProductSchema
from app.services.products.product_service import ProductService, CreateProductSchema
from app.dependencies.dependency import AccessTokenBearer

product_router = APIRouter()
product_service = ProductService()
access_token_bearer = AccessTokenBearer()


@product_router.get("/", status_code=status.HTTP_200_OK)
async def index(session: AsyncSession = Depends(get_app_session), token = Depends(access_token_bearer)):
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


# creating a new product
@product_router.post("/", status_code=status.HTTP_201_CREATED)
async def store(product_data: CreateProductSchema, session: AsyncSession = Depends(get_app_session)):
    new_product = await product_service.create_new_product(
        session = session,
        product_data = product_data
    )

    if new_product is not None:
        return new_product
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create the record")


# we will attempt to update the record here
@product_router.put("/{product_id}", status_code=status.HTTP_200_OK)
async def update(product_id: int, product_data: UpdateProductSchema, session: AsyncSession = Depends(get_app_session)):
    updated_product = await product_service.update_product(
        session = session,
        product_data = product_data,
        product_id = product_id
    )

    if updated_product is not None:
        return updated_product
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update the record with that id")


# for deleting the record here
@product_router.delete("/{product_id}", status_code=status.HTTP_200_OK)
async def destroy(product_id: int, session: AsyncSession = Depends(get_app_session)):
    product = await product_service.delete_product(session = session, product_id = product_id)
    if product is None:
        return None
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to delete the record with that id")
