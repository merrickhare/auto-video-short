import requests
import json

# function to get the quote from the API 
# Get the information form the API
# Format the response
# Parse json  and return the single fact

FACT_URL = "https://catfact.ninja/fact"

def getQuote():
    response = requests.request("GET", FACT_URL)
    formatted = response.text
    parse_json = json.loads(formatted)
    return parse_json['fact']


