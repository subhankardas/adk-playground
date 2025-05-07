import requests
import os
from dotenv import load_dotenv

load_dotenv() # load .env file

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
UNITS = "metric"

def get_weather(city: str) -> dict:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_API_KEY}&units={UNITS}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "status": "success",
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "humidity": data["main"]["humidity"],
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }