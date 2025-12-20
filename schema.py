from pydantic import BaseModel

class movie_create(BaseModel):
    title:str
    rating:float
    year:int