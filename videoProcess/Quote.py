import requests
import json
import os
from dotenv import load_dotenv

# load environment constants
load_dotenv(".env")

# function to get the quote from the API 
# Get the information form the API
# Format the response
# Parse json  and return the single fact

def get_quote():
    fact_key = os.environ["FACT_KEY"]
    response = requests.request("GET", os.environ["FACT_URL"])
    formatted = response.text
    parse_json = json.loads(formatted)
    return parse_json[fact_key]