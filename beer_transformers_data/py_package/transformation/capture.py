# py-package/transformation/capture.py

import requests

def fetch_beer_data(size=100):
    url = f"https://random-data-api.com/api/beer/random_beer?size={size}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
