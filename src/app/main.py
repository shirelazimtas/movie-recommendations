from ast import List
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from machine_learning import *
from moviebygenre import *
from wikipedia_information import *

app = FastAPI()


@app.get('/v1/{moviename}')
def movie_list(moviename: str):
    return {"recommended_movies": recommended_movies(moviename)}


@app.get('/v2/{genre}')
def populargenres(genre: str):
    return {"The_best_movies_by_genre": genres(genre)}


@app.get('/v3/wikipedia/{search}')
def info_wiki(search: str):
    return {"information_from_wikipedia": wikipedia_data(search)}


@app.get('/')
def hello():
    return {"ml-main": "hello_world"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=1234, debug=True)
