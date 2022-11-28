import requests
import json
import urllib




videoUrl = "https://api.pexels.com/videos/popular?per_page=1"
header_info = {'Authorization': '563492ad6f917000010000012b61ae83212946ee99976a1e5b0e48c7'}
response = requests.request('GET',videoUrl,headers=header_info)
format_response = response.text
parse_json = json.loads(format_response)
videoLink = parse_json['videos'][0]['video_files'][0]['link']
# urllib.request.urlretrieve(videoLink, 'saved_video.mp4') 
print(videoLink)




