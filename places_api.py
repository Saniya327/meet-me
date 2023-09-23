import json
import pprint
import gmaps
import requests
import config

def find_places(lat,long):
    #lat = 36.170216638996365
    #long = -86.79001548571094
    x_diff = 0.5/69
    y_diff = 0.25/69

    high_lat = lat + x_diff
    high_long = long + y_diff
    low_lat = lat - x_diff
    low_long = long-y_diff


    url='https://places.googleapis.com/v1/places:searchText'
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': config.API_KEY,
        'X-Goog-FieldMask':'places.displayName,places.formattedAddress,places.priceLevel'
    }
    search_query = {
        'textQuery' : 'Cafes',
        "locationRestriction": {
            "rectangle": {
                "low": {
                "latitude": low_lat,
                "longitude": low_long
                },
                "high": {
                    "latitude":high_lat,
                    "longitude": high_long
                }
            }   
        }
    }


    json_payload = json.dumps(search_query)

    response = requests.post(url, headers=headers, data=json_payload)
    json_response = json.loads(response.text)

    if response.status_code == 200:
        print('Request successful!')
        pprint.pprint(response.json())
    else:
        print('Request failed!')
        print(response.text)
