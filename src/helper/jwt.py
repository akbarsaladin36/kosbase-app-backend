
from datetime import datetime, timedelta, timezone
# from typing import Optional
from jose import JWTError, jwt
from fastapi import HTTPException, status
from src.config.settings import get_settings

settings = get_settings()

def create_token(uuid: str, username: str, email: str, role: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes = settings.jwt_access_expire_time)
    payload = {
        "uuid": uuid,
        "username": username,
        "email": email,
        "role": role,
        "exp": expire,
        "iat": datetime.now(timezone.utc)
    }
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm]
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token / token are expired!",
            headers={"WWW-Authenticate": "Bearer"}
        )
