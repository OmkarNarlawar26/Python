import requests

parameters = {
    'lat' : 20.593683,
    'lng' :78.962883,
}

response = requests.get("https://api.sunrise-sunset.org/v2", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
print(data['sunrise'])
print(data['sunset'])
