import json
import re
import sys
import nltk
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_SECRET = "YOUR_ACCESS_SECRET"
nltk.download('words')
english_words = set(nltk.corpus.words.words())
class TweetListener(StreamListener):
    def __init__(self, max_tweets=30):
        super().__init__()
        self.tweet_count = 0
        self.max_tweets = max_tweets
    def on_data(self, data):
        tweet = json.loads(data)
        self.process_tweet(tweet)
        if self.tweet_count >= self.max_tweets:
            sys.exit("Maximum number of tweets fetched.")
    def process_tweet(self, tweet):
        user_name = tweet["user"]["name"]
        verified = tweet["user"]["verified"]
        tweet_text = tweet.get("text", "")
        if "extended_tweet" in tweet:
            tweet_text = tweet["extended_tweet"]["full_text"]
        tweet_text = re.sub(r"[^A-Za-z0-9_@./]", "", tweet_text)
        with open("new_tweets.txt", "a") as output:
            output.write(f'Username: {user_name}, Verified: {verified}, Text: {tweet_text}\n')
        print(f'Username: {user_name}, Verified: {verified}, Text: {tweet_text}')
        self.tweet_count += 1
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
query_string = " ".join(sys.argv[1:])
print("Query String:", query_string)
tweet_listener = TweetListener()
twitter_stream = Stream(auth, tweet_listener)
twitter_stream.filter(languages=["en"], track=[query_string])