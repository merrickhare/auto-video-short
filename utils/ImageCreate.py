from PIL import Image, ImageDraw, ImageFont

def createImage(message):
    tweet = Image.open("images/blank_tweet.png")
    text = message
    editable = ImageDraw.Draw(tweet)
    text_font = ImageFont.truetype("~/Library/Fonts/Times New Roman", size=34)
    editable.text((85,150), text, (0, 0, 0), font=text_font)
    tweet.save("output/new_tweet21.png")

