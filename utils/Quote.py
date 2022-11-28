import requests
import json


def getQuote():
    response = requests.request("GET", "https://catfact.ninja/fact")
    formatted = response.text
    parse_json = json.loads(formatted)
    return parse_json['fact']


