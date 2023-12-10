import json
import requests


def print_news(api_key: str) -> None:
    """
    Fetches top news headlines from the NewsAPI.

    Keyword arguments:
    api_key (str): The API key to access the NewsAPI service.
    """
    base_url = "https://newsapi.org/v2/top-headlines?"
    api_key = api_key
    country = "gb"
    complete_url = base_url + "country=" + country + "&apiKey=" + api_key
    response = requests.get(complete_url)

    for article in response.json()["articles"]:
        print(article["title"])


def print_weather(api_key: str) -> None:
    """
    Fetches weather data from the OpenWeatherMap API.

    Keyword arguments:
    api_key (str): The API key to access the OpenWeatherMap service.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = api_key
    city_name = "Exeter,UK"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)

    weather = response.json()
    y = weather["main"]
    current_temperature = round(y["temp"] - 273.15, 2)
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = weather["weather"]
    weather_description = z[0]["description"]
    # print following values
    print(
        " Temperature (in degrees C) = "
        + str(current_temperature)
        + "\n atmospheric pressure (in hPa unit) = "
        + str(current_pressure)
        + "\n humidity (in percentage) = "
        + str(current_humidiy)
        + "\n description = "
        + str(weather_description)
    )


if __name__ == "__main__":
    openweatherapi_key = "7ab7a88b4612ab66297f634ee26f48b5"
    newsapi_key = "e26491fb2b9a4171a5634f0fae34d687"
