import requests

url = "https://jsonplaceholder.typicode.com/posts/6"


# # this is for PUT
# data = {
#     "id" : 6,
#     "title" : 'foo',
#     "body" : 'Barbar',
#     "userId" : 1,
# }
#
# response = requests.put(url, data)
# print(response.json())

# this is for PATCH (here we don't need to send all the data send only what the data we want to change
# data = {
#     "body" : 'Barbarbar',
# }
#
# response = requests.patch(url, data)
# print(response.json())

# this is for DELETE
data = {
    "body" : 'Barbarbar',
}

response = requests.delete(url)
print(response.json())
print(response.status_code)

