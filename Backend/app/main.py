from fastapi import FastAPI
from contextlib import asynccontextmanager
from .connection.app_database_connection import database_init
from .routes.products.product_routes import products_router


# app lifespan here
@asynccontextmanager
async def app_life_span(app: FastAPI):
    await database_init()
    yield
    print("The app is shutting down")


app_api_version = "v1"

# the route app here
app = FastAPI(
    title="Modern E-Commerce App",
    description="The Backend API for the app",
    lifespan=app_life_span,
)


app.include_router(
    router=products_router,
    tags=["products"],
    prefix=f"/E-Commerce-App/{app_api_version}/products"
)