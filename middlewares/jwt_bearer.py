from fastapi.security import HTTPBearer
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from jwt_manager import validate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['user_name'] != "arangurencg2@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales invalidas")
    