from fastapi import FastAPI
from app.routes.products.product_routes import product_router
from contextlib import asynccontextmanager
from app.connection.app_database_connection import database_init

app_api_version = "v1"


# the application life span here
@asynccontextmanager
async def app_life_span(app: FastAPI):
    await database_init()
    yield
    print("We are terminating here")


app = FastAPI(
    version=app_api_version,
    lifespan=app_life_span
)

app.include_router(
    router=product_router,
    tags=["products"],
    prefix=f"/E-Commerce-App/{app_api_version}/products"
)
