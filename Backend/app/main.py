from fastapi import FastAPI
from app.routes.products.product_routes import product_router

app_api_version = "v1"
# the routes for the app

app = FastAPI(version=app_api_version)

app.include_router(
    router=product_router,
    tags=["products"],
    prefix=f"/E-Commerce-App/{app_api_version}/products"
)
