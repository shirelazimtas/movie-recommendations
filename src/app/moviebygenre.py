from machine_learning import *
#from ml.app.machine_learning import *
import ast

# cleaning the colums genres and return the top 10 most popular movies by the genres

def genres(genre):
    if (genre.islower()):
        genre = genre.capitalize()
    movies = api_movies()
    movie_genere = movies[['title', 'genres', 'popularity']]
    for i, v in movie_genere['genres'].iteritems():
        json_arr = ast.literal_eval(movie_genere['genres'][i])
        if len(json_arr) > 0:
            movie_genere['genres'][i] = json_arr[0]['name']
        else:
            movie_genere['genres'][i] = 0
    sorted_df = movie_genere.sort_values(
        by=['genres', 'popularity'], ascending=False)
    sorted_df = sorted_df.dropna()
    title = sorted_df.loc[sorted_df['genres'] == genre]
    title = title['title'].head(10)
    arr_title = title.to_numpy()
    arr_title = arr_title.tolist()
    return arr_title

