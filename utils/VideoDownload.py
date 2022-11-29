import requests
import json
from constants import VIDEOURL, AUTH_TOKEN


# Request stored in response variable
response = requests.request('GET',VIDEOURL,headers=AUTH_TOKEN)

# Format the response 
format_response = response.text

# Parse json 
parse_json = json.loads(format_response)

# Grab the external video link
videoLink = parse_json['videos'][0]['video_files'][0]['link']


# Print for testing 
print(videoLink)




