from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session
from database import get_db,create_table
import models,schema

app=FastAPI()

create_table()

@app.get('/movie')
def get_all(db:Session=Depends(get_db)):
    return db.query(models.Movie).all()


@app.post('/movie')
def create_new(mov:schema.movie_create,db:Session=Depends(get_db)):
    new_mov=models.Movie(**mov.model_dump())
    db.add(new_mov)
    db.commit()
    db.refresh(new_mov)
    return new_mov