import json
import requests
# from dotenv import load_dotenv
import os

OMDB_API_KEY = os.getenv("OMDB_API_KEY")
google_api_key = ""

def omdb_api_call(str):
    movie_url = "http://www.omdbapi.com/?apikey=" + OMDB_API_KEY + "&t=" + str
    response = requests.get(movie_url)
    json_load = json.loads(response.text)
    return (json_load)

# json response is available in the dictionary "json_load" http://www.omdbapi.com/ for available reponses.






