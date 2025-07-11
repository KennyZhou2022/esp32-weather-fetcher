import os
import requests
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def fetch_weather():
    api_key = os.getenv("API_KEY")
    http_proxy = os.getenv("HTTP_PROXY")
    https_proxy = os.getenv("HTTPS_PROXY")

    if not api_key:
        raise ValueError("API_KEY is not set")

    lat = "31.2222"
    lon = "121.4581"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    proxies = {
        "http": http_proxy,
        "https": https_proxy
    }

    response = requests.get(url, proxies=proxies, timeout=20)
    response.raise_for_status()

    data = response.json()

    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    history_path = f"/data/history_weather/weather_{timestamp}.json"
    latest_path = "/data/weather_latest.json"

    with open(history_path, "w", encoding="utf-8") as f:
        f.write(response.text)

    with open(latest_path, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"✅ Weather data saved to {latest_path} and {history_path}")


def fetch_pollution():
    api_key = os.getenv("API_KEY")
    http_proxy = os.getenv("HTTP_PROXY")
    https_proxy = os.getenv("HTTPS_PROXY")

    if not api_key:
        raise ValueError("API_KEY is not set")

    lat = "31.2222"
    lon = "121.4581"

    # Calculate the start time (24 hours from now)
    end_time = int(datetime.utcnow().timestamp())
    start_time = end_time - (3600 * (24 - 1))

    url = (
        f"https://api.openweathermap.org/data/2.5/air_pollution/history"
        f"?lat={lat}&lon={lon}&start={start_time}&end={end_time}&appid={api_key}"
    )

    proxies = {
        "http": http_proxy,
        "https": https_proxy
    }

    response = requests.get(url, proxies=proxies, timeout=20)
    response.raise_for_status()

    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    history_path = f"/data/history_pollution/pollution_{timestamp}.json"
    latest_path = "/data/pollution_latest.json"

    with open(history_path, "w", encoding="utf-8") as f:
        f.write(response.text)

    with open(latest_path, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"✅ Pollution data saved to {latest_path} and {history_path}")