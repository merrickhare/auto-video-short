import requests
import json
import urllib.request
from random import randint

VIDEOURL = "https://api.pexels.com/videos/search?query=cats&orientation=portrait&per_page=49"
AUTH_TOKEN = {'Authorization': '563492ad6f917000010000012b61ae83212946ee99976a1e5b0e48c7'}

def downloadVideo():
    # Create random number between 0 and 49
    random_index = randint(0,49)

    # Request stored in response variable
    response = requests.request('GET',VIDEOURL,headers=AUTH_TOKEN)

    # Format the response 
    format_response = response.text

    # Parse json 
    parse_json = json.loads(format_response)

    # Grab the external video link
    videoLink = parse_json['videos'][random_index]['video_files'][0]['link']

    # Download the video file
    urllib.request.urlretrieve(videoLink, "output/downloaded.mp4")





