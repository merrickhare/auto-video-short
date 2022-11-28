import requests
import json


# function to get the quote from the API 
# Get the information form the API
# Format the response
# Parse json  and return the single fact

def getQuote():
    response = requests.request("GET", "https://catfact.ninja/fact")
    formatted = response.text
    parse_json = json.loads(formatted)
    return parse_json['fact']


