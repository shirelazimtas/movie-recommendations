import json
from urllib import response
from pandas import options
from requests import request
import requests
import streamlit as st 
import os
from PIL import Image

def json_to_str(json_object):
    json_data = json.loads(json_object)
    str_movie_name=" "
    for the_key, the_value in json_data.items():
        str_movie_name = the_key
    str_movie_name = str_movie_name + ": "
    for the_key, the_value in json_data.items():
        for v in the_value:
            str_movie_name = str_movie_name + v
            str_movie_name = str_movie_name + ", "
    return str_movie_name

def json_wiki(json_object):
    json_data = json.loads(json_object)
    str_movie_name=" "
    for the_key, the_value in json_data.items():
        str_movie_name = the_key
    str_movie_name = str_movie_name + ": "
    for the_key, the_value in json_data.items():
        for v in the_value:
            str_movie_name = str_movie_name + v
            str_movie_name = str_movie_name + " "
    return str_movie_name

#CURRENT_THEME = "blue"


st.markdown("<h1 style='text-align: center; color: white;'>MOVIE RECOMMENDED</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: grey;'>THE BEST WEBSITE</h2>", unsafe_allow_html=True)


image = Image.open('movie_pic.png')
st.image(image)
st.balloons()

moviename=st.text_input("Please insert one lovely movie name, and we will make sure you recieve movies that you will surely love")
if moviename:
    req_recommrnded= requests.get(f"http://web:1234/v1/{moviename}")
    response_recommanded=json_to_str(req_recommrnded.text)
    st.text(response_recommanded)
else:
    st.warning("Please type movie name!")    

gener=st.selectbox("Here you can select a genre and get the TOP 10 movies in the genre",options=["Action", "Adventure" ,"Animation","Comedy" ,"Crime" ,"Drama" ,"Family" ,"Fantasy" ,"Film-Noir" ,"History" ,"Horror" ,"Mystery" ,"Romance" ,"Sci-Fi" ,"Sport","War","Western"],format_func=lambda x: 'Select an option' if x == '' else x
 )
if gener:
    st.success('Yay! 🎉')
    req_gener=requests.get(f"http://web:1234/v2/{gener}")
    response_jenre = json_to_str(req_gener.text)
    response_jenre
else:
    st.warning('No option is selected')

movie_wikipedia=st.text_input("You can write the movie name you would like to watch to get summery from the wikipedia")
if movie_wikipedia:
    st.success('Yay! 🎉')
    req_wikipedia=requests.get(f"http://web:1234/v3/wikipedia/{movie_wikipedia}")
    response_wikipedia=json_wiki(req_wikipedia.text)
    st.text(response_wikipedia)
else:
    st.warning("Please type movie name!")   









