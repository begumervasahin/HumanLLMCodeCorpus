import json
from config import SETTINGS
from TwitterAPI import TwitterAPI
b1 = "tweets.json"
b2 = TwitterAPI(
    SETTINGS["consumer_key"],
    SETTINGS["consumer_secret"],
    SETTINGS["access_token_key"],
    SETTINGS["access_token_secret"]
)
def fonk1(query):
    return b2.request('search/tweets', {'q': query})
def fonk2(username):
    return b2.request('statuses/user_timeline', {'screen_name': username, 'count': 200})
def fonk3(username, filename):
    with open(filename, 'a+') as tweet_file:
        for tweet in fonk2(username):
            json.dump(tweet, tweet_file, b3 = (',', ':'))
            tweet_file.write('\n')
def fonk4():
    fonk3("hasgeek", b1)
if b4 = = "__main__":
    fonk4()