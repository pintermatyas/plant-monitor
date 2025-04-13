import requests
from time import sleep
from prometheus_client import start_http_server, Gauge

temp_gauge = Gauge('outside_temperature', 'Current temperature in Budapest (°C)')
humidity_gauge = Gauge('outside_humidity_percentage', 'Current relative humidity in Budapest (%)')

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 47.4979,
        "longitude": 19.0402,
        "current": "temperature_2m,relative_humidity_2m"
    }
    response = requests.get(url, params=params)
    data = response.json()

    current = data.get("current", {})
    temperature = current.get("temperature_2m")
    humidity = current.get("relative_humidity_2m")

    if temperature is not None:
        temp_gauge.set(temperature)
        print(f"Temperature: {temperature}°C")
    if humidity is not None:
        humidity_gauge.set(humidity)
        print(f"Humidity: {humidity}%")

def main():
    start_http_server(8002)
    while True:
        try:
            fetch_weather()
        except Exception as e:
            print("Failed to fetch weather:", e)
        sleep(60) # Update every minute

if __name__ == "__main__":
    main()
