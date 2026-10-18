import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : 'foo',
    "body" : 'We are testint post request',
    "userId" : 1,
}

response = requests.post(url, json=data)
print(response.content)
if response.status_code == 201:
    print("Success")
else:
    print("Failed")
