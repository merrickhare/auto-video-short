from gtts import gTTS
from os import environ
from dotenv import load_dotenv

#load environment constants
load_dotenv(".env")
AUDIO = environ["AUDIO_NAME"]
# function that takes the text quote and outputs a speech file

def makeAudio(quote):
    message = quote
    speech = gTTS(message)
    speech.save(f"output/{AUDIO}")