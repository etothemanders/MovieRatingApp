import model
import csv
import datetime

def load_users(session):
    # use u.user
    with open("./seed_data/u.user", "rb") as f:
        reader = csv.reader(f)
        for row in reader:
             user = row[0]
             user_id, age, gender, occupation, zipcode = user.split("|")
             user = model.User(id=int(user_id), age=int(age), gender=gender, occupation=occupation, zipcode=zipcode)
             s.add(user)
    s.commit()

def load_movies(session):
    # use u.item
    with open("./seed_data/u.item", "rb") as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            movie = row
            # assign movie attributes
            movie_id = movie[0].decode("latin-1")
            title = movie[1].decode("latin-1")

            # convert release date to datetime format
            released_at = movie[2].decode("latin-1")
            if released_at != "":
                released_at = datetime.datetime.strptime(released_at, "%d-%b-%Y")
            else:
                released_at = datetime.datetime.now()

            # continue to assign movie attributes
            imdb_url = movie[4].decode("latin-1")
            genre_unknown = int(movie[5].decode("latin-1"))
            genre_Action = int(movie[6].decode("latin-1"))
            genre_Adventure = int(movie[7].decode("latin-1"))
            genre_Animation = int(movie[8].decode("latin-1"))
            genre_Childrens = int(movie[9].decode("latin-1"))
            genre_Comedy = int(movie[10].decode("latin-1"))
            genre_Crime = int(movie[11].decode("latin-1"))
            genre_Documentary = int(movie[12].decode("latin-1"))
            genre_Drama = int(movie[13].decode("latin-1"))
            genre_Fantasy = int(movie[14].decode("latin-1"))
            genre_FilmNoir = int(movie[15].decode("latin-1"))
            genre_Horror = int(movie[16].decode("latin-1"))
            genre_Musical = int(movie[17].decode("latin-1"))
            genre_Mystery = int(movie[18].decode("latin-1"))
            genre_Romance = int(movie[19].decode("latin-1"))
            genre_SciFi = int(movie[20].decode("latin-1"))
            genre_Thriller = int(movie[21].decode("latin-1"))
            genre_War = int(movie[22].decode("latin-1"))
            genre_Western = int(movie[23].decode("latin-1"))

            movie = model.Movie(id = movie_id, name = title, released_at=released_at, 
                imdb_url=imdb_url, genre_unknown=genre_unknown, 
                genre_Action=genre_Action, genre_Adventure=genre_Adventure, 
                genre_Animation=genre_Animation, genre_Childrens=genre_Childrens, 
                genre_Comedy=genre_Comedy, genre_Crime=genre_Crime, 
                genre_Documentary=genre_Documentary, genre_Drama=genre_Drama, 
                genre_Fantasy=genre_Fantasy, genre_FilmNoir=genre_FilmNoir, 
                genre_Horror=genre_Horror, genre_Musical=genre_Musical, 
                genre_Mystery=genre_Mystery, genre_Romance=genre_Romance, 
                genre_SciFi=genre_SciFi, genre_Thriller=genre_Thriller, 
                genre_War=genre_War, genre_Western=genre_Western)
            s.add(movie)
    s.commit()

def load_ratings(session):
    # use u.data
    with open("./seed_data/u.data", "rb") as f:
        reader = csv.reader(f)
        for row in reader:
             rating = row[0]
             user_id, item_id, rating, timestamp = rating.split("\t")
             rating = model.Rating(user_id=user_id, movie_id=item_id, rating=rating)
             s.add(rating)
    s.commit()

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    pass

if __name__ == "__main__":
    s= model.connect()
    main(s)
