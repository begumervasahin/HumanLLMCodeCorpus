import json
from TwitterAPI import TwitterAPI
SETTINGS = {
    "consumer_key": "your_consumer_key",
    "consumer_secret": "your_consumer_secret",
    "access_token_key": "your_access_token_key",
    "access_token_secret": "your_access_token_secret"
}
FILE_NAME = "tweets.json"
def get_search_query(query, api):
    data = api.request('search/tweets', {'q': query})
    return data
def get_user_timeline(username, api):
    data = api.request('statuses/user_timeline', {'screen_name': username, 'count': 200})
    return data
def run():
    """
    Call this function to save/append tweets containing "fifthel" to tweets.json
    """
    api = TwitterAPI(
        SETTINGS["consumer_key"],
        SETTINGS["consumer_secret"],
        SETTINGS["access_token_key"],
        SETTINGS["access_token_secret"]
    )
    tweet_file = open(FILE_NAME, 'a+')
    for item in get_user_timeline("hasgeek", api).get_iterator():
        json.dump(item, tweet_file, separators=(',', ':'))
        tweet_file.write('\n')
        tweet_file.flush()
    tweet_file.close()
if __name__ == "__main__":
    run()