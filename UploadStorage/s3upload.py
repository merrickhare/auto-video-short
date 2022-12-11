import boto3
import os
from logging import exception
from dotenv import load_dotenv


# load environment constants
load_dotenv(".env")

# function to start a new session and upload to 
def uploadVideo(videoName):
    try:
        session = boto3.Session(profile_name=os.environ["PROFILE"])
        s3 = session.client('s3')
        s3.upload_file(f"output/{videoName}",os.environ["BUCKET"],videoName)  
        return True
    except exception as e:
        print(f"Oops something went wrong: {e}")

    


 


