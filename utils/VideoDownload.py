import requests
import json

# API URL
videoUrl = "https://api.pexels.com/videos/popular?per_page=1"

# Auth Token
header_info = {'Authorization': '563492ad6f917000010000012b61ae83212946ee99976a1e5b0e48c7'}

# Request stored in response variable
response = requests.request('GET',videoUrl,headers=header_info)

# Format the response 
format_response = response.text

# Parse json 
parse_json = json.loads(format_response)

# Grab the external video link
videoLink = parse_json['videos'][0]['video_files'][0]['link']


# Print for testing 
print(videoLink)




