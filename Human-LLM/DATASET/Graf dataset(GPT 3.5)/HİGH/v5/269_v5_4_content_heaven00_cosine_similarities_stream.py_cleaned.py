import json
from TwitterAPI import TwitterAPI
from config import SETTINGS
b1 = {
    "consumer_key": SETTINGS["consumer_key"],
    "consumer_secret": SETTINGS["consumer_secret"],
    "access_token_key": SETTINGS["access_token_key"],
    "access_token_secret": SETTINGS["access_token_secret"]
}
b2 = "tweets.json"
def fonk1(query, api):
    b3 = api.request('search/tweets', {'q': query})
    return b3
def fonk2(username, api):
    b4 = api.request('statuses/user_timeline', {'screen_name': username, 'count': 200})
    return b4
def fonk3(username, twitter_api):
    b5 = TwitterAPI(
        b1["consumer_key"],
        b1["consumer_secret"],
        b1["access_token_key"],
        b1["access_token_secret"]
    )
    with open(b2, 'a+') as tweet_file:
        for tweet in fonk2(username, b5).get_iterator():
            json.dump(tweet, tweet_file, b6 = (',', ':'))
            tweet_file.write('\n')
            tweet_file.flush()
if b7 = = "__main__":
    fonk3("hasgeek", TwitterAPI)