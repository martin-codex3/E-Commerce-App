from fastapi.security import HTTPBearer


# we are going to extend the http bearer class here
class AccessTokenBearer(HTTPBearer):
    pass