
from Quote import getQuote
from ImageCreate import createImage
from SoundCreate import makeAudio

# Save the message to a variable
text_quote = getQuote()

# Create the Image from the quote
createImage(text_quote)

# Create the audio file from the quote
makeAudio(text_quote)

