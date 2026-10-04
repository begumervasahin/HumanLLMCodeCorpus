
import json
from config import SETTINGS
from TwitterAPI import TwitterAPI
FILE_NAME = "tweets.json"
API = TwitterAPI(SETTINGS["consumer_key"], SETTINGS["consumer_secret"],\
            SETTINGS["access_token_key"], SETTINGS["access_token_secret"])
def get_search_query(query):
    data = API.request('search/tweets', {'q':query})
    return data
def get_user_timeline(username):
    data = API.request('statuses/user_timeline', {'screen_name':username,'count':200})
    return data
def run():
    tweet_file = open(FILE_NAME, 'a+')
    for item in get_user_timeline("hasgeek").get_iterator():
        json.dump(item, tweet_file, separators=(',', ':'))
        tweet_file.write('\n')
        tweet_file.flush()
if __name__ == "__main__":
    run()