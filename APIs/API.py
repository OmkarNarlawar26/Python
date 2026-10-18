import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")

# print(response.content)
# print(response.status_code)
# print(response.raise_for_status())

response.raise_for_status()
print(response.json()['setup'])
print(response.json()['punchline'])