from sqlalchemy import Column,Integer,String,Float
from database import Base

class Movie(Base):

    __tablename__='Movie'
    
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,index=True)
    rating=Column(Float)
    year=Column(Integer)

