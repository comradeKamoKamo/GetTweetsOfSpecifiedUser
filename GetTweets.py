import json , os
from collections import OrderedDict
import tweepy

class GetTweets:

    def __init__(self,path_json):
        d = OrderedDict()
        with open(path_json,"r") as f:
            d = json.loads(f.read())
        api_key = d["api_key"]
        api_secret = d["api_secret"]
        access_token = d["access_token"]
        access_token_secret = d["access_token_secret"]

        auth = tweepy.OAuthHandler(api_key,api_secret)
        auth.set_access_token(access_token,access_token_secret)
        self.api = tweepy.API(auth)

    def get_tweets(self,username,exclude_replies):
        self.tweets = []
        for tweet in tweepy.Cursor(self.api.user_timeline,
            screen_name = username,
            exclude_replies = exclude_replies).items():
            self.tweets.append(
                [tweet.id,tweet.created_at,tweet.text.replace('\n',''),
                tweet.favorite_count,tweet.retweet_count])
        return self.tweets