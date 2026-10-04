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
    b3 = b2.request('search/tweets', {'q': query})
    return b3
def fonk2(username):
    b3 = b2.request('statuses/user_timeline', {'screen_name': username, 'count': 200})
    return b3
def fonk3(username, filename):
    with open(filename, 'a+') as tweet_file:
        for tweet in fonk2(username):
            json.dump(tweet, tweet_file, b4 = (',', ':'))
            tweet_file.write('\n')
            tweet_file.flush()
if b5 = = "__main__":
    fonk3("hasgeek", b1)