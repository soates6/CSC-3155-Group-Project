from jose import JWTError, jwt
from datetime import datetime, timedelta
import os

# Load the secret key and algorithm from environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def create_confirmation_token(email: str):
    """
    Create a JWT token with the user's email, expiring in 1 hour.
    """
    expire = datetime.utcnow() + timedelta(hours=1)
    to_encode = {"exp": expire, "email": email}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_confirmation_token(token: str):
    """
    Verify a JWT token and extract the email from its payload.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("email")
    except JWTError:
        return None
