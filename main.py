
from videoProcess.Quote import getQuote
from videoProcess.SoundCreate import makeAudio
from videoProcess.VideoDownload import downloadVideo
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from textwrap import fill
from UploadStorage.s3upload import uploadVideo
from os import environ
from dotenv import load_dotenv
import datetime

# Created By: Merrick Hare
# Date: 11/27/2022
# Website: https://merrickhare.com
# GitHub: https://github.com/merrickhare

#load environment constants
load_dotenv(".env")
AUDIO_NAME = environ["AUDIO_NAME"]
VIDEO_NAME = environ["VIDEO_NAME"]
FINAL_VIDEO = environ["FINAL_VIDEO"]
UPLOAD = environ["UPLOAD"]
videoDay = datetime.datetime.now()
videoDay.strftime("%m-%d-%M")

try:
    # Save the message to a variable
    text_quote = getQuote()

    # Create the audio file from the quote
    makeAudio(text_quote)

    # Grab video from API and download to output folder
    downloadVideo()

    # Assemble the final video 
    text_quote = fill(text_quote,width=30,fix_sentence_endings=True)

    resolution = (1080,1920)

    audio_clip = AudioFileClip(f"output/{AUDIO_NAME}")

    video_clip = VideoFileClip(f"output/{VIDEO_NAME}", audio=False,).set_audio(audio_clip).loop(duration = audio_clip.duration).resize(resolution)

    fact_text = TextClip(text_quote, color='white', fontsize=50).set_position(('center', 1050))

    final = CompositeVideoClip([video_clip,fact_text],size=resolution)

    final.subclip(0, video_clip.duration).write_videofile(f"output/{FINAL_VIDEO}", fps=30, codec='libx264')
    
    # Upload the video to AWS S3 Bucket

    if UPLOAD == True: 
        uploadVideo(f"{FINAL_VIDEO}")

except Exception as e:

    print(f"Exception:  {e}")

