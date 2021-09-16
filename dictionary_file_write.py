import json
import popcorn_api

data = popcorn_api.omdb_api_call("scream")

with open('convert.txt', 'w') as convert_file:
    convert_file.write(json.dumps(data))
