import json
from TwitterAPI import TwitterAPI
TWITTER_SETTINGS = {
    "consumer_key": "your_consumer_key",
    "consumer_secret": "your_consumer_secret",
    "access_token_key": "your_access_token_key",
    "access_token_secret": "your_access_token_secret"
}
FILE_NAME = "tweets.json"
def get_search_results(query, api):
    search_data = api.request('search/tweets', {'q': query})
    return search_data
def get_user_tweets(username, api):
    user_tweets_data = api.request('statuses/user_timeline', {'screen_name': username, 'count': 200})
    return user_tweets_data
def save_tweets_with_keyword(keyword, twitter_api):
    twitter_connection = TwitterAPI(
        TWITTER_SETTINGS["consumer_key"],
        TWITTER_SETTINGS["consumer_secret"],
        TWITTER_SETTINGS["access_token_key"],
        TWITTER_SETTINGS["access_token_secret"]
    )
    with open(FILE_NAME, 'a+') as tweet_file:
        for tweet in get_user_tweets(keyword, twitter_connection).get_iterator():
            json.dump(tweet, tweet_file, separators=(',', ':'))
            tweet_file.write('\n')
            tweet_file.flush()
if __name__ == "__main__":
    save_tweets_with_keyword("hasgeek", TwitterAPI)