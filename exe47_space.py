#Lets find who is in space!!!

"""Lets pull the data directly from the open-notify API.
Parse the Json file to learn about the people in space."""

import requests
import json

space = requests.get('http://api.open-notify.org/astros.json')

space_dict = json.loads(space.text)

#check the data from from the api
#print(space_dict['people'])

print("Name             |Craft")
print("-----------------|-------")

for people in space_dict['people']:
    print(people['name'], "|", people['craft'])
    people["last name"] = people["name"].split()[-1]

sorted_spacers = sorted(space_dict['people'], key=lambda x: x['last name'])
print("Lets print sorted spacers...\n\n")
#print(sorted_spacers)

for people in sorted_spacers:
    print(people['name'], "|", people['craft'])
