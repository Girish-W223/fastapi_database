from typing import List
from fastapi import FastAPI,HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db,create_table
import models,schema

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=['*']
)

create_table()

@app.get('/movie',response_model=List[schema.movie_show])
def get_all(db:Session=Depends(get_db)):
    movie_data=db.query(models.Movie).all()
    #print(movie_data[0].id)
    return movie_data

@app.post('/movie')
def create_new(mov:schema.movie_create,db:Session=Depends(get_db)):
    new_mov=models.Movie(**mov.model_dump())
    db.add(new_mov)
    db.commit()
    db.refresh(new_mov)
    return new_mov


@app.get('/movie/{m_id}')
def get_movie(m_id:int,db:Session=Depends(get_db)):
    return db.query(models.Movie).filter(models.Movie.id==m_id).first()



@app.put('/movie/{m_id}')
def update(m_id:int,mov:schema.movie_create,db:Session=Depends(get_db)):
    data=db.query(models.Movie).filter(models.Movie.id==m_id).first()
    if data:
        for key,val in mov.model_dump().items():
            setattr(data,key,val)
        db.commit()
        db.refresh(data)
    return data



@app.delete('/movie/{m_id}')
def delete(m_id:int , db:Session=Depends(get_db)):
    data=db.query(models.Movie).filter(models.Movie.id==m_id).first()
    if data:
        db.delete(data)
        db.commit()
    return data


