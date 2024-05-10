from pydantic import BaseModel
from fastapi import APIRouter
from jwt_manager import create_token
from fastapi.responses import JSONResponse

class User(BaseModel):
    user_name: str
    password:str


    class Config:
        schema_extra= {
            'schema':{
                'id': 1,
                'movie': 'Mi pelicula',
                'category': 'Accion',
                'year': 2024
            }
        }
user_router = APIRouter()

@user_router.post('/login', tags=['auth'], response_model=None)
def auth_user(user: User):
    if user.user_name == "arangurencg2@gmail.com" and user.password== "admin":
        token : str = create_token(user.model_dump())
        return JSONResponse(content=token, status_code=200)
    return JSONResponse(content={"message": "user or password invalid"}, status_code=303)
