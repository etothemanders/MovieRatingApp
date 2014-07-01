from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker
import datetime
ENGINE = None
Session = None

Base = declarative_base()

### Class declarations go here

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable = True)
    age = Column(Integer, nullable = True)
    gender = Column(String(10), nullable=True)
    occupation = Column(String(64), nullable=True)
    zipcode = Column(String(15), nullable = True)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    released_at = Column(DateTime)
    imdb_url = Column(String(64))
    genre_unknown = Column(Integer)
    genre_Action = Column(Integer)
    genre_Adventure = Column(Integer)
    genre_Animation = Column(Integer)
    genre_Childrens = Column(Integer)
    genre_Comedy = Column(Integer)
    genre_Crime = Column(Integer)
    genre_Documentary = Column(Integer)
    genre_Drama = Column(Integer)
    genre_Fantasy = Column(Integer)
    genre_FilmNoir = Column(Integer)
    genre_Horror = Column(Integer)
    genre_Musical = Column(Integer)
    genre_Mystery = Column(Integer)
    genre_Romance = Column(Integer)
    genre_SciFi = Column(Integer)
    genre_Thriller = Column(Integer)
    genre_War = Column(Integer)
    genre_Western = Column(Integer)


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer)
    user_id = Column(Integer)
    rating = Column(Integer)

### End class declarations

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
