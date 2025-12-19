from passlib.context import CryptContext


my_context = CryptContext(
    schemes=["argon2"]
)

# function to get the hashed password
def get_hashed_password(password: str) -> str:
    password_hash = my_context.hash(password)
    return password_hash


# function to verify the password
def verify_password(password: str, password_hash) -> bool:
    return my_context.verify(password, password_hash)