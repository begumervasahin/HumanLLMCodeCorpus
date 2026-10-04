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
    response = api.request('search/tweets', {'q': query})
    return response
def get_user_timeline(username):
    response = api.request('statuses/user_timeline', {'screen_name': username, 'count': 200})
    return response
def save_tweets_to_file():
    with open(FILE_NAME, 'a+') as tweet_file:
        for tweet in get_user_timeline("hasgeek").get_iterator():
            json.dump(tweet, tweet_file, separators=(',', ':'))
            tweet_file.write('\n')
            tweet_file.flush()
if __name__ == "__main__":
    save_tweets_to_file()