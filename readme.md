# Video Shorts Cat Fact Bot 
<em>This is a personal project to continue learning Python.</em>

### YouTube Channel:
https://www.youtube.com/channel/UCOLn1O_aNc2gmbecBSmsSIw

# Updates
Created a function in SoundCreate.py to use AWS Polly for voice. It grabs a random voice from the US English list each time for the voice over. **Must have AWS account** to use. 

The gTTS function is available to use and can be swapped out in main.py if needed. 

# Required:
<em>https://www.pexels.com API Authorization Token</em>\
<em>`brew install ffmpeg`</em>\
<em>`brew install imagemagick`</em>\
<em>`pip3 install moviepy`</em>\
<em>`pip3 install gTTS`</em>\
<em>`pip3 install dotenv`</em>
<em>`pip3 install boto3`</em>

### Edit config.env and Save file As .env.
### Unless using s3 for storage do not uncomment in main.py. 


# To Do List:

1. Automate upload to youtube channel

# Notes: 

Quote.py - Uses requests library to grab a cat "fact" from a free api and formats the json response.

SoundCreate.py - Uses gTTS library to take the quote from Quote.py and turn it into an audio file. Includes function for AWS Polly and will grab random voice for each video. 

main.py - This will call all of the functions.

VideoDownload.py - Downloads the video to be used as the background

# Resources:

Video API \
<em>https://www.pexels.com/api/documentation/</em> 

gTTS \
<em>https://gtts.readthedocs.io/en/latest/</em>

AWS Polly \
<em>https://docs.aws.amazon.com/polly/latest/dg/what-is.html</em>











