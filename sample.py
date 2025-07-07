import requests

url = "http://44.222.195.104:8000//predict"
payload = { "user_id" : "3" }

response = requests.post(url, json=payload)
print(response.json())