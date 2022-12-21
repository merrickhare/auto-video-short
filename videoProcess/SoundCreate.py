from gtts import gTTS
from os import environ
from dotenv import load_dotenv
import boto3
from random import randint

#load environment constants
load_dotenv(".env")
AUDIO = environ["AUDIO_NAME"]
PROFILE = environ["PROFILE"]

# create a client session for AWS polly voice synthesis
client = boto3.Session(profile_name=PROFILE).client("polly")

# function that takes the text quote and outputs a speech file

def make_audio(quote):
    message = quote
    speech = gTTS(message)
    speech.save(f"output/{AUDIO}")

# Function to use AWS polly instead of gTTS
def polly_audio(quote):
    voices = ["Kimberly","Kendra","Joanna","Ivy","Kevin","Matthew","Justin","Joey"]
    randName = randint(0,7)
    response = client.synthesize_speech(
        VoiceId = voices[randName],
        OutputFormat = "mp3",
        Text = quote,
        Engine = "neural"
    )
    file = open(f"output/{AUDIO}", "wb")
    file.write(response['AudioStream'].read())
    file.close()
