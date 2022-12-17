from gtts import gTTS
from os import environ
from dotenv import load_dotenv
import boto3

#load environment constants
load_dotenv(".env")
AUDIO = environ["AUDIO_NAME"]
PROFILE = environ["PROFILE"]
client = boto3.Session(profile_name=PROFILE).client("polly")

# function that takes the text quote and outputs a speech file

def makeAudio(quote):
    message = quote
    speech = gTTS(message)
    speech.save(f"output/{AUDIO}")

def pollyAudio(quote):
    response = client.synthesize_speech(
        VoiceId = "Joanna",
        OutputFormat = "mp3",
        Text = quote,
        Engine = "neural"
    )
    file = open(f"output/{AUDIO}", "wb")
    file.write(response['AudioStream'].read())
    file.close()
