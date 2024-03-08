#Who told we can't catch the weather!!!

import requests
import json

where = input("Where are you now?")

print(f"{where} weather is:")

piz = f"https://api.openweathermap.org/data/2.5/weather?q={where}&APPID=9c689fed7df2fe5993f95af012e8e684"

get_data = requests.get(piz)

load_data = json.loads(get_data.text)

def conv_temp(num:int,from_scale:str, to_scale:str) -> int:
    """Returns the temperature from any scale to 
    any temperature scale..."""
    if from_scale == 'F' and to_scale == 'C':
        conv = (num - 32)* (5/9)
        return round(conv , 2)
    elif from_scale == 'K' and to_scale == 'C':
        conv =  (num - 273.15)
        return round(conv, 2)
    elif from_scale == 'C' and to_scale == 'F':
        conv =  (num * (9/5)) + 32
        return round(conv, 2)
    elif from_scale == 'K' and to_scale == 'F' :
        conv = (num - 273.15) * (9/5) + 32
        return round(conv, 2)
    elif from_scale == 'C' and to_scale == 'K':
        conv = (num + 273.15)
        return round(conv, 2)
    else: 
        conv = (num - 32)* (5/9) + 273.15
        return round(conv, 2)


print(f"Weather description is {load_data['weather'][0]['description']}")

tempC = conv_temp(load_data['main']['temp'],from_scale='K',to_scale='C')

print(f"Temperature is {tempC}")