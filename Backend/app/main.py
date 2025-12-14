from fastapi import FastAPI
from contextlib import asynccontextmanager
from .connection.app_database_connection import database_init
# app lifespan here
@asynccontextmanager
async def app_life_span(app: FastAPI):
    await database_init()
    yield
    print("The app is shutting down")


# the route app here
app = FastAPI(
    title="Modern E-Commerce App",
    description="The Backend API for the app",
    lifespan=app_life_span,
)


@app.get("/")
async def root():
    return {"message": "hello world here"}