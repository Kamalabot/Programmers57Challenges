#lets get some movie reviews from RottenTomatoes

"""
Script will access the Rotten Tomatoes API and get the review
details for the movie you search for. The program is incomplete
because the API is not working.
"""
from urllib.parse import quote

apikey = "pgejx5vbmtarkka2g2jkn4tf"
baseUrl = "http://api.rottentomatoes.com/api/public/v1.0"


moviesSearchUrl = baseUrl + '/movies.json?apikey=' + apikey
query = quote("Gone with the Wind")

get_query = moviesSearchUrl + '&q=' + query

import requests
import json

get_text = requests.get(get_query)

print(get_text.text)

#load_data = json.loads(get_text)

#print(load_data)