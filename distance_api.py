
import json
import requests
import config
from datetime import datetime

#TODO: try the routes api 

#gmaps = googlemaps.Client(key=config.API_KEY)

url='https://maps.googleapis.com/maps/api/distancematrix/json'
params={
   'destinations':'909 Flats Nashville',
   'origins':'UBS tower Nashville',
   'units':'imperial',
   'mode':'walking',
   'key':config.API_KEY
}


response=requests.get(url,params=params)
json_data = json.loads(response.text)

if response.status_code == 200:
    #print('Request successful!')
    #pprint.pprint(data)
    distance = json_data['rows'][0]['elements'][0]['distance']['text']
    unit = distance[-2:]
    distance_num=distance[:-2]
    print(distance_num)
    print(unit)
else:
    print('Request failed!')
    print(response.text)
