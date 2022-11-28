from gtts import gTTS

def makeAudio(quote):
    message = quote
    speech = gTTS(message)
    speech.save("output/audofile22.mp3")