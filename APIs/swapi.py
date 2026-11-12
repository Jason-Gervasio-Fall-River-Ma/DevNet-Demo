import requests
import json

base_url = "https://swapi.dev/api/"
endpoint = "planets/"

#Response object from the API call
#This will contain the status code, headers, and the body of the response.
response = requests.get(base_url + endpoint)

data = response.json()
print(data['results'][0]['terrain'])