import requests
import json

response = requests.request("GET", "https://catfact.ninja/fact")
formatted = response.text.split(", ")
print(formatted)
