
import json
import requests
import config

def find_mid_distance(origin, destination):
    url='https://maps.googleapis.com/maps/api/distancematrix/json'
    params={
        'destinations':destination,
        'origins':origin,
        'units':'imperial',
        'mode':'walking',
        'key':config.API_KEY
    }


    response=requests.get(url,params=params)
    json_response = json.loads(response.text)

    if response.status_code == 200:
        distance = json_response['rows'][0]['elements'][0]['distance']['text']
        unit = distance[-2:]
        distance=distance.replace(",", "")
        distance_num=distance[:-2]
        return float(distance_num)/2
    else:
        print('Request failed!')
        print(response.text)
        return None