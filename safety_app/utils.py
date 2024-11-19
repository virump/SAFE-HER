# tracking/utils.py

import requests

def get_nearby_police_stations(latitude, longitude):
    api_key = 'your_google_places_api_key'
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=5000&type=police&key={api_key}"
    response = requests.get(url)
    results = response.json().get('results', [])
    return [place['name'] for place in results]
