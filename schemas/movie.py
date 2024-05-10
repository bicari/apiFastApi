from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id:Optional[int] | None = None
    title: str = Field(min_length=5, max_length=20)
    category: str = Field(min_length=5, max_length=20)
    year: int = Field(default=2024, le=2024)
    rating: int = Field(default=10)

movies=  [{
    'id': 2,
    'title':'AvATAR',
    'category':'Disney',
    'year':'2009'
},
{'id':4,
   'title': 'Frozen',
   'category':'Peror',
   'year':'2008'}]