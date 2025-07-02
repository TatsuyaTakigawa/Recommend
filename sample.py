import requests

url = "http://ec2-3-236-219-100.compute-1.amazonaws.com:8000/predict"
payload = { "user_id" : "3" }

response = requests.post(url, json=payload)
print(response.json())