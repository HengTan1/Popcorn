from flask import Flask
import popcorn_api

app = Flask (__name__)

@app.route('/')
def test():
    return popcorn_api.omdb_api_call("scream")

#Should just need to do "flask run" in cmd to get this to run on local host "127.0.0.1:5000"
