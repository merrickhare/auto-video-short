# Youtube Shorts Video Maker
<em>This is a personal project not intended for use by the community until completed. </em>

### To Do List:

1. Download free video
2. Download free music track
3. Format JSON response
4. Put it all together using moviepy

### Completed:

1. Connected to the cat "facts" API
2. Create audio file from the cat facts
3. Grabbing a single quote from API
4. Storing created assests in output folder

### Notes: 

ImageCreate.py - Uses Pillow library to take the quote from Quote.py and overlay it onto the template image.

Quote.py - Uses requests library to grab a cat "fact" from a free api and formats the json response.

SoundCreate.py - Uses Google Text To Speech library to take the quote from Quote.py and turn it into an audio file.

main.py - This will call all of the functions to do the following: 

1. Generate the quote
2. Create the image
3. Create the sound file
4. Edit the generated files into a single mp4
5. Save all output files to output folder



<em>Creator: Merrick Hare \
Maintainer: Merrick Hare \
Contributors: { }
</em>






