from models.movie import Movie as MoviesL
from schemas.movie import Movie

class MovieService():
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MoviesL).all()
        return result
    
    def get_query_movie(self, category):
        result = self.db.query(MoviesL).filter(MoviesL.category == category).all()
        return result
    
    def get_movie_id(self, id):
        result = self.db.query(MoviesL).filter(MoviesL.id == id).first()
        return result

    def create_movie(self, movie: Movie):
        create_movie = MoviesL(**movie.dict())
        self.db.add(create_movie)
        self.db.commit()
        return  

    def update_movie(self, id, movie: Movie):
        result_movie = self.get_movie_id(id)
        result_movie.title = movie.title
        result_movie.category = movie.category
        result_movie.year = movie.year
        result_movie.rating = movie.rating
        self.db.commit()
        return

    def delete_movie(self, movie: Movie):
        self.db.delete(movie)
        self.db.commit()
        return