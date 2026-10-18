import requests

api_key = "2c6e3f5320a20e36d80d3f3516fe38d7"
endpoint = "http://api.openweathermap.org/data/2.5/weather?"
api_params = {
    "q" : "Paris",
    "appid" : api_key,
}

response = requests.get(endpoint, params=api_params)
print(response.json())


