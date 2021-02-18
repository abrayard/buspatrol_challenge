import requests

url = "http://127.0.0.1:5000"

response = requests.get(url + "/users/maurice")
print(response.json())