# Video Shorts Cat Fact Bot 
<em>This is a personal project to continue learning Python.</em>

### Required:
<em>https://www.pexels.com API Authorization Token</em>\
<em>brew install ffmpeg</em>\
<em>brew install imagemagick</em>\
<em>pip install moviepy</em>\
<em>pip install gTTS</em>\
<em>pip install dotenv</em>

### Edit config.env and Save file As .env.
### Unless using s3 for storage do not uncomment in main.py. 


## To Do List:

1. Automate upload to youtube channel

## Notes: 

Changing the 

Quote.py - Uses requests library to grab a cat "fact" from a free api and formats the json response.

SoundCreate.py - Uses gTTS library to take the quote from Quote.py and turn it into an audio file.

main.py - This will call all of the functions.

VideoDownload.py - Downloads the video to be used as the background

## Resources:

Video API \
<em>https://www.pexels.com/api/documentation/</em> 

gTTS \
<em>https://gtts.readthedocs.io/en/latest/</em>












