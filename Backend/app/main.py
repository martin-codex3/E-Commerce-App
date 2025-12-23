from fastapi import FastAPI
from app.routes.products.product_routes import product_router
from contextlib import asynccontextmanager
from app.connection.app_database_connection import database_init
from app.routes.auth.auth_routes import auth_router
from app.config.app_config import AppConfig

# for the middlewares here
from fastapi.middleware.cors import CORSMiddleware

app_api_version = "v1"

# the application life span here
@asynccontextmanager
async def app_life_span(app: FastAPI):
    await database_init()
    yield
    return


app = FastAPI(
    version=app_api_version,
    lifespan=app_life_span,
    title="Backend API",
    description="The full featured api to manage all the backend tasks for the app"
)

# for the allowed origins here
origins = [
    AppConfig.ALLOWED_ORIGIN_ONE,
    AppConfig.ALLOWED_ORIGIN_TWO,
    AppConfig.ALLOWED_ORIGIN_THREE,
]

# for the allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_headers = ["*"],
    allow_methods = ["*"]
)

app.include_router(
    router=product_router,
    tags=["products"],
    prefix=f"/api"
)

# authentication routes here
app.include_router(
    router=auth_router,
    tags=["authentication"],
    prefix=f"/api"
)