from gtts import gTTS


def create_audio():
    message = "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma - which is living with the results of other people's thinking. Don't let the noise of others' opinions drown out your own inner voice. And most important, have the courage to follow your heart and intuition."
    speech = gTTS(message)
    speech.save("audofile2.mp3")
