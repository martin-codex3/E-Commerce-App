import jwt
from datetime import timedelta


# function to encode the jwt token
def encode_jwt_token(user_data: dict, expiry: timedelta = None, refresh: bool = False) -> str:
    