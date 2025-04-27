import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
REQUEST_URL = "https://api.api-ninjas.com/v1/animals?name="

if not API_KEY:
    raise EnvironmentError("API_KEY not found in environment variables.")

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.

    Args:
        animal_name (str): The name of the animal to fetch data for.

    Returns:
        list: A list of animals, each represented as a dictionary.
    """
    url = REQUEST_URL + animal_name
    try:
        response = requests.get(url, headers={'X-Api-Key': API_KEY}, timeout=5)
        response.raise_for_status()
        return response.json()  # Expected to be a list of animal dictionaries
    except requests.RequestException as e:
        print(f"Error fetching data for '{animal_name}': {e}")
        return []
