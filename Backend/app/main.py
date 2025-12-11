from fastapi import FastAPI
from routes.auth.AuthRoutes import auth_router

# the app version here
app_version = "v1"

# we will register the routes here
app = FastAPI(
    version=app_version,
    title="The Backend Api for the modern E-Commerce App",
    description="This app will have all the advanced features to match every business needs",
)

# we will add the app here
app.include_router(
    router=auth_router,
    tags=["auth"],
    prefix=f"/E-commerce-app/{app_version}/auth"
)