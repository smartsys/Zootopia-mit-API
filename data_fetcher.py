import os

import requests
from dotenv import load_dotenv
load_dotenv()

URL = str(os.getenv("URL"))
API_KEY = str(os.getenv("API_KEY"))


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    """
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}
    response = requests.get(URL, headers=headers, params=params)
    return response.json()
