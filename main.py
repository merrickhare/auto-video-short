
from videoProcess.Quote import getQuote
from videoProcess.ImageCreate import createImage
from videoProcess.SoundCreate import makeAudio
from videoProcess.VideoDownload import downloadVideo
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

video_clip = VideoFileClip('output/downloaded.mp4', audio=False)
audio_clip = AudioFileClip('output/audiofile.mp3')
video_clip = video_clip.set_audio(audio_clip)
video_clip = video_clip.loop(duration = audio_clip.duration)
fact_text = TextClip(text_quote, color='black', fontsize=12).set_position(('center','center'))
final = CompositeVideoClip([video_clip,fact_text])
final.subclip(0, video_clip.duration).write_videofile("output/newfile.mp4", fps=24, codec='libx264')