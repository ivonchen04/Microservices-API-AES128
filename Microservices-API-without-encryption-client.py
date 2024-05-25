import requests

message = {"message": "Hello, Server!"}
response = requests.post("http://127.0.0.1:5000/message", json=message)
print(response.json())
