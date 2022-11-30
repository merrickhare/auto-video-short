
from utils.Quote import getQuote
from utils.ImageCreate import createImage
from utils.SoundCreate import makeAudio
from utils.VideoDownload import downloadVideo
from moviepy.editor import *


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

# Assemble the final video 

# get the output video

video_clip = VideoFileClip('output/downloaded.mp4',audio=False)
fact_text = TextClip("Test Quote String", color='black', fontsize=20)
final = CompositeVideoClip([video_clip,fact_text])
final.subclip(0,15).write_videofile("output/newfile.mp4", fps=24, codec='libx264')