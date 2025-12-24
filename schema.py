from pydantic import BaseModel

class movie_create(BaseModel):
    title:str
    rating:float
    year:int

class movie_show(movie_create):
    id:int
    class Config():
        from_attribute=True        