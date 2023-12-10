import api_functions
import json
import time
from datetime import datetime


def get_api_keys(filename="api_keys.json") -> dict:
    """
    Gets a dictionary of API keys from a JSON file.

    Keyword arguments:
    filename (str): The name of the JSON file containing the API keys. Default  ("api_keys.json")
    """
    # Opens the JSON file containing the API keys
    with open(filename, "r") as api_file:
        api_keys = json.load(api_file)
    # Gets a dictionary of API keys from api_keys.json
    api_keys = api_keys.get("API-keys", {})
    # Gets the NewsAPI API key from the dictionary
    newsapi_key = api_keys.get("newsapi_key")
    # Gets the OpenWeatherMap API key from the dictionary
    openweatherapi_key = api_keys.get("openweatherapi_key")
    return newsapi_key, openweatherapi_key


# Gets the API keys from the JSON file
newsapi_key, openweatherapi_key = get_api_keys()
# Gets news data from the NewsAPI every 5 mins
while True:
    start = time.time()
    print("News: as of " + str(datetime.now()))
    api_functions.print_news(newsapi_key)
    end = time.time()
    print(f"Got news in: {round((end - start)*1000,1)}ms...")
    time.sleep(60 * 5)  # 5 mins
