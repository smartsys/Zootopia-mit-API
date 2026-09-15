import json
import os

import requests
from dotenv import load_dotenv
load_dotenv()

url = str(os.getenv("URL"))
api_key = str(os.getenv("API_KEY"))


def fetch_data(animal_name):
    """Ruft Tiere passend zu einem Namen von der API Ninjas Animals API ab.

    Args:
        animal_name (str): Gebräuchlicher Name des gesuchten Tiers.
            Teiltreffer werden unterstützt, z.B. findet "fox" auch "Arctic Fox".

    Returns:
        list[dict]: Bis zu 10 passende Tiere, jeweils mit den Schlüsseln
            'name', 'taxonomy', 'locations' und 'characteristics'.
    """
    headers = {"X-Api-Key": api_key}
    params = {"name": animal_name}
    response = requests.get(url, headers=headers, params=params)
    # print(" DEBUG")
    # print(" animal_name:", animal_name)
    # print(" status_code:", response.status_code)
    # print(" response.json:", response.json())
    # print("")
    return response.json()



def get_animal_details(animal_name):
    """Ruft Tiere per Namen ab und reduziert sie auf die Felder der Tierkarte.

    Fehlende Eigenschaften werden mit 'N/A' belegt, ein fehlender Name mit
    'Unbekannt'. Von 'locations' wird nur der erste Eintrag verwendet.

    Args:
        animal_name (str): Gebräuchlicher Name des gesuchten Tiers.

    Returns:
        list[dict]: Ein Dict pro Tier mit den Schlüsseln 'name', 'diet',
            'location', 'type', 'temperament' und 'skin_type'.
    """
    animals = fetch_data(animal_name)
    details = []
    for animal in animals:
        characteristics = animal.get('characteristics', {})
        details.append({
            'name': animal.get('name', 'Unbekannt'),
            'diet': characteristics.get('diet', 'N/A'),
            'location': animal.get('locations', [])[0],
            'type': characteristics.get('type', 'N/A'),
            'temperament': characteristics.get('temperament', 'N/A'),
            'skin_type': characteristics.get('skin_type', 'N/A'),
        })
    return details


def main():
    for animal in get_animal_details("fox"):
        print(animal['name'])
        print(f"Diet: {animal['diet']}")
        print(f"Location: {animal['location']}")
        print(f"Type: {animal['type']}")
        print(f"Temperament: {animal['temperament']}")
        print(f"Skin type: {animal['skin_type']}")
        print()