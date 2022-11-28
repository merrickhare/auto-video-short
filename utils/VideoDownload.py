import requests

videoUrl = "https://api.pexels.com/videos/search?query=nature&per_page=1"
header_info = {'Authorization': '563492ad6f917000010000012b61ae83212946ee99976a1e5b0e48c7'}
response = requests.get(url=videoUrl, headers=header_info)
print(response.text)