import logging

import jwt
from datetime import timedelta, datetime

from sqlalchemy.sql.coercions import expect

from app.config.app_config import AppConfig


jwt_key = AppConfig.JWT_KEY
jwt_algorithm = AppConfig.JWT_ALGORITHM

# function to encode the jwt token
def encode_jwt_token(user_data: dict, expiry: timedelta = None, refresh: bool = False) -> str:
    payload = {
        "user": user_data,
        "exp": datetime.now() + (expiry if expiry is not None else timedelta(minutes=60)),
        "iat": datetime
    }

    token = jwt.encode(
        payload = payload,
        key=jwt_key,
        algorithm=jwt_algorithm
    )

    return token


# function to decode the toke  here
def decode_jwt_token(jwt_token: str):
    try:
        token = jwt.decode(
            algorithms=[AppConfig.JWT_ALGORITHM],
            key=AppConfig.JWT_KEY,
            jwt=jwt_token
        )

        return token
    except jwt.PyJWTError as error:
        logging.exception(error)
        return None

    except Exception as e:
        logging.exception(e)
        return None

