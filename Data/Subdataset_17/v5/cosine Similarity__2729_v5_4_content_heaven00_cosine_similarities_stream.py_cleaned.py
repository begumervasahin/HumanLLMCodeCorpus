import json
from config import SETTINGS
from TwitterAPI import TwitterAPI
FILE_NAME = "tweets.json"
api = TwitterAPI(
    SETTINGS["consumer_key"],
    SETTINGS["consumer_secret"],
    SETTINGS["access_token_key"],
    SETTINGS["access_token_secret"]
)
def get_search_query(query):
    return api.request('search/tweets', {'q': query})
def get_user_timeline(username):
    return api.request('statuses/user_timeline', {'screen_name': username, 'count': 200})
def save_tweets_to_file(username, filename):
    with open(filename, 'a+') as tweet_file:
        for tweet in get_user_timeline(username):
            json.dump(tweet, tweet_file, separators=(',', ':'))
            tweet_file.write('\n')
def run():
    save_tweets_to_file("hasgeek", FILE_NAME)
if __name__ == "__main__":
    run()