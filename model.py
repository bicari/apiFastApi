from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    user: str
    password:str

class Movie(BaseModel):
    id:Optional[int] | None = None
    movie: str = Field(min_length=5, max_length=20)
    category: str = Field(min_length=5, max_length=20)
    year: int = Field(default=2024, le=2024)


    class Config:
        schema_extra= {
            'schema':{
                'id': 1,
                'movie': 'Mi pelicula',
                'category': 'Accion',
                'year': 2024
            }
        }