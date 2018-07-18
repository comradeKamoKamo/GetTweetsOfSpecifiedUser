import json , os
from collections import OrderedDict
import tweepy

class GetTweets:

    def __init__(self,path_json):
        s = open(path_json).read()
        d = json.loads(s)

        api_key = d["api_key"]
        api_secret = d["api_secret"]
        access_token = d["access_token"]
        access_token_secret = d["access_token_secret"]

        auth = tweepy.OAuthHandler(api_key,api_secret)
        auth.set_access_token(access_token,access_token_secret)
        self.api = tweepy.API(auth)



        