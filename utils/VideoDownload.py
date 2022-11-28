import requests

videoUrl = ""
response = requests.request("GET",videoUrl)
print(response.text)