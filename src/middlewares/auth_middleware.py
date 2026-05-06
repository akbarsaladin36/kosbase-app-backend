from fastapi import Request, status, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from src.config.settings import get_settings

bearer_scheme = HTTPBearer(auto_error=True)
settings = get_settings()

def _get_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> str:
    return credentials.credentials

def user_authentication(req: Request, token: str = Depends(_get_token)) -> dict:
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=settings.jwt_algorithm)
        req.state.current_user = payload
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token / token is expired!",
            headers={"WWW-Authenticate": "Bearer"}
        )

def user_role_required(*allowed_roles: str):

    def user_check_role(req: Request, current_user: dict = Depends(user_authentication)) -> dict:
        user_role = current_user.get("role")

        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Invalid role access! {user_role} not have permission!"
                       f"Role can access={', '.join(allowed_roles)}"
            )

        return current_user 

    return user_check_role
