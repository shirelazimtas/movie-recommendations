# import
from kaggel_key import *
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import process
import importlib_metadata
import pandas as pd
import os
import ast
from pyparsing import matchPreviousExpr
pd.options.mode.chained_assignment = None



username_key = key_value()


def api_movies():
    os.environ['KAGGLE_USERNAME'] = username_key.username
    os.environ['KAGGLE_KEY'] = username_key.key
    from kaggle.api.kaggle_api_extended import KaggleApi
    from zipfile import ZipFile
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file(
        'rounakbanik/the-movies-dataset', 'movies_metadata.csv')
    zf = ZipFile('movies_metadata.csv.zip')
    zf.extractall()
    zf.close()
    data = pd.read_csv('movies_metadata.csv', dtype='unicode')
    return data


def api_ratings():
    os.environ['KAGGLE_USERNAME'] = username_key.username
    os.environ['KAGGLE_KEY'] = username_key.key
    from kaggle.api.kaggle_api_extended import KaggleApi
    from zipfile import ZipFile
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file(
        'rounakbanik/the-movies-dataset', 'ratings_small.csv')
    zf = ZipFile('ratings_small.csv.zip')
    zf.extractall()
    zf.close()
    rating_data = pd.read_csv('ratings_small.csv', dtype='unicode')
    return rating_data


# clean the data frame to get better result and make matrix
# in X-axis there is userId and for y-axis there is movieId, vote average, popularity
# on the matrix has votes to each movie

def data_clening():
    movies = api_movies()
    rating_dataframe = api_ratings()
    rating_dataframe['userId'] = rating_dataframe['userId'].astype(
        str).astype(float)
    data_vote = movies[['id', 'vote_average', 'popularity']]
    data_vote.columns = ['movieId', 'vote_average', 'popularity']
    movies_users = rating_dataframe.pivot(
        index='movieId', columns='userId', values='rating').fillna(0)
    movies_user = movies_users.copy()
    movie_user_popular = pd.merge(movies_user, data_vote, on='movieId')
    movie_user_popular = movie_user_popular.dropna(
        how='any', axis=0, thresh=673)
    s = movie_user_popular.columns
    movie_user_popular[s] = movie_user_popular[s].astype(str).astype(float)
    return movie_user_popular


# Machine learning KNN
def recommender_knn(movie_name, movie_user_popular, n):
    arr = []
    modle = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=2)
    modle.fit(movie_user_popular)
    movies = api_movies()
    index = process.extractOne(movie_name, movies['title'])[2]
    ll = movies.loc[index, 'id']
    n_row = process.extractOne(
        str(float(ll)), movie_user_popular['movieId'])[2]
    distances, indices = modle.kneighbors(
        movie_user_popular[movie_user_popular.index == n_row], n_neighbors=n)
    list_id = []
    for i in indices[0]:
        list_id.append(int(movie_user_popular.loc[i, 'movieId']))
    for n in list_id:
        strid = str(n)
        x = process.extractOne(strid, movies['id'])[2]
        if(movies.loc[x, 'title'] != movies.loc[index, 'title']):
            arr.append(movies.loc[x, 'title'])

    return arr


def recommended_movies(movie_name):
    movie_user_popular = data_clening()
    x = recommender_knn(movie_name, movie_user_popular, 7)
    return x
