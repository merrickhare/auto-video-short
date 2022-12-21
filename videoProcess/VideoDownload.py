import requests
import json
import urllib.request
import ast
from random import randint
from os import environ
from dotenv import load_dotenv

#load environment constants
load_dotenv(".env")


VIDEOURL = environ["VIDEOURL"]
AUTH_TOKEN = ast.literal_eval(environ["AUTH_TOKEN"])
VIDEO_NAME = environ["VIDEO_NAME"]

def download_video():
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
    urllib.request.urlretrieve(videoLink, f"output/{VIDEO_NAME}")




