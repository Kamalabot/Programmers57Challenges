#Pixabay some photos...

"""Here I will use the Pixabay API to get some photos.
Code will be extended with additional """

import json
import requests
#from urllib.parse import quote
from bs4 import BeautifulSoup

s_term = input("Enter your search term: ")
s_term = s_term.replace(" ", "+")


req = f"https://pixabay.com/api/?key=yourapikey&q={s_term}&image_type=photo"
print(req)

get_images = requests.get(req)

image_data = json.loads(get_images.text)

#print(image_data)

hits = image_data["hits"]

for hit in hits:
    print(hit["tags"])
    print(hit["previewURL"])
    print(hit["id"])
    print("\n")