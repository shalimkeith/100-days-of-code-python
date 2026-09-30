import requests

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "aee034502c4b2c82de1366e2c2a86968"

weather_params = {
    "lat": 24.86,
    "lon": 63.01,
    "appid": api_key,
}

response = requests.get(OWN_Endpoint, params=weather_params)
print(response.status_code)
print(response.json())