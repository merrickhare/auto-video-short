# Youtube Shorts Video Maker
<em>This is a personal project not intended for use by the community until completed. </em>

### To Do List:
1. Generate video from assets using moviePY

### Completed:

1. Connected to the cat "facts" API
2. Create audio file from the cat facts
3. Grabbing a single quote from API
4. Storing created assests in output folder
5. Download video in portrait mode from Pexels

### Notes: 

ImageCreate.py - Uses Pillow library to take the quote from Quote.py and overlay it onto the template image.

Quote.py - Uses requests library to grab a cat "fact" from a free api and formats the json response.

SoundCreate.py - Uses gTTS library to take the quote from Quote.py and turn it into an audio file.

main.py - This will call all of the functions to do the following: 

1. Generate the quote
2. Create the image
3. Create the sound file
4. Edit the generated files into a single mp4
5. Save all output files to output folder

### Resources:

Video API \
<em>https://www.pexels.com/api/documentation/</em> 

gTTS \
<em>https://gtts.readthedocs.io/en/latest/</em>












