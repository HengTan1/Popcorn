import json
import requests
import os
import imdb

ia = imdb.IMDb()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")
google_api_key = ""

def omdb_api_call(str):
    movie_url = "http://www.omdbapi.com/?apikey=" + OMDB_API_KEY + "&t=" + str
    response = requests.get(movie_url)
    json_load = json.loads(response.text)
    return (json_load)

def top_movies_imdb():
    top = ia.get_top250_movies()
    top_5 = [top[0]['title'], top[1]['title'], top[2]['title'], top[3]['title'], top[4]['title'], top[5]['title']]
    str_top_5 = str(top_5)
    return str_top_5

def worst_movies_imdb():
    worst = ia.get_bottom100_movies()
    worst_5 = [worst[0]['title'], worst[1]['title'], worst[2]['title'], worst[3]['title'], worst[4]['title'], worst[5]['title']]
    str_worst_5 = str(worst_5)
    return str_worst_5


# json response is available in the dictionary "json_load" http://www.omdbapi.com/ for available reponses.






