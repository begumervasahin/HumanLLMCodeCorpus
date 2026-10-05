import json
import re
import sys
import nltk
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
ckey = "YOUR_CONSUMER_KEY"
csecret = "YOUR_CONSUMER_SECRET"
atoken = "YOUR_ACCESS_TOKEN"
asecret = "YOUR_ACCESS_SECRET"
nltk.download('words')
words = set(nltk.corpus.words.words())
class MyStreamListener(StreamListener):
    tweet_count = 0
    def on_data(self, data):
        tweet_data = json.loads(data)
        with open("new_tweets.txt", "a") as output:
            user_name = tweet_data["user"]["name"].encode('utf-8')
            verified = tweet_data["user"]["verified"]
            tweet_text = tweet_data["text"].encode('utf-8')
            if "extended_tweet" in tweet_data:
                tweet_text = tweet_data["extended_tweet"]["full_text"].encode('utf-8')
            tweet_text = re.sub(r"[^A-Za-z0-9_@./]", "", tweet_text)
            print(f'Username: {user_name}, Verified: {verified}, Text: {tweet_text}')
            output.write(f'Username: {user_name}, Verified: {verified}, Text: {tweet_text}\n')
            MyStreamListener.tweet_count += 1
            if MyStreamListener.tweet_count == 30:
                sys.exit("30 tweets fetched")
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
query_string = " ".join(sys.argv[1:])
print("Query String:", query_string)
twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(languages=["en"], track=[query_string])