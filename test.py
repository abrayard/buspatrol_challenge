import requests
import json

url = "http://127.0.0.1:5000"

response = requests.get(url + "/users/gene")
user_info = json.loads(response.content)
print(json.dumps(user_info, indent=0))

#print(response.json()) # This does the job as well but does not indent the values in the JSON data. 
