from gtts import gTTS

# function that takes the text quote and outputs a speech file

def makeAudio(quote):
    message = quote
    speech = gTTS(message)
    speech.save("output/audiofile.mp3")