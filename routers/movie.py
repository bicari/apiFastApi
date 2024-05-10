from fastapi import APIRouter
from fastapi import Path, Query,  Depends
from fastapi.responses import JSONResponse
from schemas.movie import Movie
from middlewares.jwt_bearer import JWTBearer
from config.database import Session
from services.movie import MovieService
from fastapi.encoders import jsonable_encoder



movie_router = APIRouter()

@movie_router.get('/movies/{id}', tags=['Movies'], status_code=200, dependencies=[Depends(JWTBearer())])
def search_movie(id: int = Path(ge=1, le=2000)):
    db = Session()
    pelis=MovieService(db).get_movie_id(id)
    if not pelis:
        return JSONResponse(status_code=404, content={'message': 'Recurso no encontrado'})
    return JSONResponse(content=jsonable_encoder(pelis)) 

@movie_router.get('/movies', tags=['Movies'])
def search_all_movie():
    db = Session()
    pelis_category = MovieService(db).get_movies()
    if not pelis_category:
        return JSONResponse(status_code=404, content={'message': 'Categoria no encontrada'})
    return JSONResponse(status_code=200,content=jsonable_encoder(pelis_category))

@movie_router.get('/movies/', tags=['Movies'])
def search_movie_query(category: str = Query(min_length=5, max_length=15)):
    db = Session()
    pelis_category = MovieService(db).get_query_movie(category)
    if not pelis_category:
        return JSONResponse(status_code=404, content={'message': 'Categoria no encontrada'})
    return JSONResponse(status_code=200,content=jsonable_encoder(pelis_category))

@movie_router.post('/movies', tags=['Movies'], status_code=201, dependencies=[Depends(JWTBearer())])
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Pelicula registrada exitosamente"})

@movie_router.put('/movies/{id}', tags=['Movies'])
def update_movie(id:int , movie: Movie):
    db = Session()
    result = MovieService(db).get_movie_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Recurso no encontrado'})
    MovieService(db).update_movie(id, movie)    
    return JSONResponse(status_code=200, content={'message': 'Pelicula actualizada'})

@movie_router.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id:int):
    db = Session()
    result= MovieService(db).get_movie_id(id)
    if not result:
        return JSONResponse(status_code=404 ,content={"message": "Recurso no econtrado"})
    MovieService(db).delete_movie(result)   
    return JSONResponse(status_code=200, content={"message": f"Pelicula {result.title} eliminada con exito"})