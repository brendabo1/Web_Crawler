import tweepy
from dotenv import load_dotenv
import os
import gdown

class Bot:
    def __init__(self) -> None:
        load_dotenv() 
        consumer_key = os.getenv("CONSUMER_KEY")
        consumer_secret = os.getenv("CONSUMER_SECRET")

        access_token = os.getenv("ACCESS_TOKEN")
        access_secret = os.getenv("ACCESS_TOKEN_SECRET")
        bearer_token = os.getenv("BEARER_TOKEN")

        self.client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_secret,
            bearer_token=r"{}".format(bearer_token)
        )
 
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
        auth.set_access_token(
            access_token,
            access_secret
        )
        self.api = tweepy.API(auth)

    def post(self, data: dict):
        try:
            # image_link = data["image"]

            # media = None
            # if image_link != "":
            #     path = "temp/{}.jpg".format(str(data["date"]))
            #     gdown.download(image_link, path)
            #     media = self.api.media_upload(filename=path)

            post = "{}\n\Score Anterior{}\n\Score Atual:{}\n\nLink: {}".format(
                data["title"],
                data["old_score"],
                data["score"],
                data["link"]
            )
            self.client.create_tweet(text=post)
            # if media is not None:
            #     self.client.create_tweet(text=post, media_ids=[media.media_id])
            # else:
            #     self.client.create_tweet(text=post)
            return True
        
        except Exception as e:
            print(str(e))
            return False
        