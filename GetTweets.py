import json , csv
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
        self.__api = tweepy.API(auth)

    def get_tweets(self,username,exclude_replies=True):
        self.tweets = []
        for tweet in tweepy.Cursor(self.__api.user_timeline,
            screen_name = username,
            exclude_replies = exclude_replies).items():
            if (not tweet.retweeted) and ('RT @' not in tweet.text):
                self.tweets.append(
                    [tweet.id,tweet.created_at,tweet.text.replace('\n',''),
                    tweet.favorite_count,tweet.retweet_count])

    def save_tweets(self,path_save):
        with open(path_save,"w",encoding="utf-8") as f:
            writer = csv.writer(f,lineterminator='\n')
            writer.writerow(["id","created_at","text","fav","RT"])
            writer.writerows(self.tweets)
