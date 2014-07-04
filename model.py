from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session, joinedload
import datetime
import correlation

engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                         autocommit = False,
                         autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

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

    def similarity(self, other):
        u_ratings = {}
        paired_ratings = []
        for r in self.ratings:
            u_ratings[r.movie_id] = r

        for r in other.ratings:
            u_r = u_ratings.get(r.movie_id)
            if u_r:
                paired_ratings.append( (u_r.rating, r.rating) )

        if paired_ratings:
            return correlation.pearson(paired_ratings)
        else:
            return 0.0

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
    movie_id = Column(Integer, ForeignKey('movies.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Integer)

    user = relationship("User", backref=backref("ratings", order_by=id))
    movie = relationship("Movie", backref=backref("ratings", order_by=id))

### End class declarations
### Begin other functions

def add_user(email, password, age, gender, occupation, zipcode):
    new_user = User(email=email, password=password, age=age, gender=gender, occupation=occupation, zipcode=zipcode)
    session.add(new_user)
    session.commit()  
    return "successfully added new user"

def get_user_by_email_password(email, password):
    user = session.query(User).filter_by(email=email).filter_by(password=password).one()
    if user:
        return user
    else:
        return False

def add_rating_record(movie_id, user_id, rating):
    new_rating = Rating(movie_id=movie_id, user_id=user_id, rating=rating)
    session.add(new_rating)
    session.commit()
    return "Successfully added new movie rating"

def get_movie_id_by_title(title):
    movie = session.query(Movie).filter_by(name=title).one()
    if movie:
        return movie.id

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
