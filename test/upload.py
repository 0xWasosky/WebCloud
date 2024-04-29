import requests


url = "http://127.0.0.1:8080/upload"
payload = {"file": open("file.txt", 'rb').read()}

response = requests.post(url, files=payload)

print(response.json())
