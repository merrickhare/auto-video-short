
from utils.Quote import getQuote
from utils.ImageCreate import createImage
from utils.SoundCreate import makeAudio
from utils.VideoDownload import downloadVideo


# Created By: Merrick Hare
# Date: 11/27/2022
# Website: https://merrickhare.com
# GitHub: https://github.com/merrickhare


# Save the message to a variable
text_quote = getQuote()

# Create the Image from the quote
createImage(text_quote)

# Create the audio file from the quote
makeAudio(text_quote)

# Grab video from API and download to output folder
downloadVideo()

