import json
import pprint
import requests
import config
import places_api

def find_mid_distance():
    url='https://maps.googleapis.com/maps/api/distancematrix/json'
    params={
        'destinations':'909 Flats Nashville',
        'origins':'2010 West End Ave Nashville',
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
        return float(distance_num)/2
    else:
        print('Request failed!')
        print(response.text)
        return None


url='https://maps.googleapis.com/maps/api/directions/json'
params={
   'destination':'909 Flats Nashville',
   'origin':'2010 West End Ave Nashville',
   'mode':'walking',
   'key':config.API_KEY
}

distance_ref = float(find_mid_distance())
response=requests.get(url,params=params)
json_data = json.loads(response.text)

if response.status_code == 200:
    steps = json_data['routes'][0]['legs'][0]['steps']
    distance_sum=0;
    for step in steps:
        
        distance=step['distance']['text']
        unit = distance[-2:]
        distance_num=distance[:-2]
      
        if unit == 'ft':
            distance_num = float(distance_num) * 0.000189394
        distance_sum+=float(distance_num)
        print(distance_sum)
        if(distance_sum >= distance_ref):
            lat = step['end_location']['lat']
            lng = step['end_location']['lng']
            places_api.find_places(lat,lng)
            break
    print(distance_ref)
    print(distance_sum)
else:
    print('Request failed!')
    print(response.text)
    


