
from videoProcess.Quote import getQuote
from videoProcess.SoundCreate import makeAudio
from videoProcess.VideoDownload import downloadVideo
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from textwrap import fill



# Created By: Merrick Hare
# Date: 11/27/2022
# Website: https://merrickhare.com
# GitHub: https://github.com/merrickhare

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
    audio_clip = AudioFileClip('output/audiofile.mp3')
    video_clip = VideoFileClip('output/downloaded.mp4', audio=False,).set_audio(audio_clip).loop(duration = audio_clip.duration).resize(resolution)
    fact_text = TextClip(text_quote, color='white', fontsize=50).set_position(('center', 1050))
    final = CompositeVideoClip([video_clip,fact_text],size=resolution)
    final.subclip(0, video_clip.duration).write_videofile("output/newfile.mp4", fps=30, codec='libx264')
except Exception as e:
    print(f"Exception:  {e}")