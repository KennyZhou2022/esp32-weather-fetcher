import time
from fetch_weather import fetch_weather, fetch_pollution

print("[*] Start fetching weather information")

while True:
    try:
        fetch_weather()
        fetch_pollution()
    except Exception as e:
        print(f"[!] Exception: {e}")
    time.sleep(600)  # Fetch data every 10 mins
