from fastapi import FastAPI
from app.routes.auth.AuthRoutes import auth_router
from app.routes.products.ProductsRoutes import products_router
from contextlib import asynccontextmanager
from app.connection.db_connection import db_init

# the app version here
app_version = "v1"

# the life span for the app here
@asynccontextmanager
async def life_span(app: FastAPI):
    print("The app is starting")
    await db_init()
    yield
    print("The app is shutting down")

# we will register the routes here
app = FastAPI(
    version=app_version,
    title="The Backend Api for the modern E-Commerce App",
    description="This app will have all the advanced features to match every business needs",
    lifespan=life_span
)

# we will add the app here
app.include_router(
    router=auth_router,
    tags=["auth"],
    prefix=f"/E-commerce-app/{app_version}/auth"
)

# we will inject the other router here
app.include_router(
    router=products_router,
    tags=["auth"],
    prefix=f"/E-commerce-app/{app_version}/products"
)