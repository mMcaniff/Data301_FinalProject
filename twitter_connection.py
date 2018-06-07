import tweepy
import config
import codecs
from tweet import Tweet
from tweepy import OAuthHandler


def process_and_store(file, tweet):
    _tweet = Tweet(tweet)
    file.write(_tweet.__str__().replace('\n','') + "\n")


def connect(user_name):
    file = codecs.open("files/" + user_name + ".txt", 'a', "utf-8")

    auth = OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)

    api = tweepy.API(auth)
    n = 0
    page_list = []

    pages = tweepy.Cursor(api.user_timeline, screen_name=user_name, include_rts=False, count=200).pages(16)

    for page in tweepy.Cursor(api.user_timeline, screen_name=user_name, include_rts=False, count=200).pages(16):
        page_list.append(page)
        n = n+1
        print("Gathering Data " + user_name + ": " + str((n*.0625)*100) + "%")
    for page in page_list:
        for tweet in page:
            process_and_store(file, tweet)