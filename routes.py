import json
import sys
import requests
import config
import places_api
import distance_api
destination=sys.argv[1]
origin=sys.argv[2]
url='https://maps.googleapis.com/maps/api/directions/json'
params={
   'destination':destination,
   'origin':origin,
   'mode':'walking',
   'key':config.API_KEY
}

distance_ref = float(distance_api.find_mid_distance(origin,destination))
response=requests.get(url,params=params)
json_response = json.loads(response.text)

if response.status_code == 200:
    steps = json_response['routes'][0]['legs'][0]['steps']
    distance_sum=0
    
    for step in steps: 
        distance=step['distance']['text']
        unit = distance[-2:]
        distance_num=distance[:-2]
      
        if unit == 'ft':
            distance_num = float(distance_num) * 0.000189394
        distance_sum+=float(distance_num)
    
        if(distance_sum >= distance_ref):
            lat = step['end_location']['lat']
            lng = step['end_location']['lng']
            places_api.find_places(lat,lng)
            break
else:
    print('Request failed!')
    print(response.text)
    


