import tweepy
import json
import nltk
import re
import sys
CONSUMER_KEY = "ZmPXKTWphyiVnQxlCa2erNy64"
CONSUMER_SECRET = "gI3B2iQflMbB166VFI55Gll84S7I8Izb73iyaWoMTyc2QdU4HU"
ACCESS_TOKEN = "2697779004-2Pk3eVHdgdHYtsnbDxGjKEopbh5moyVER09hHDV"
ACCESS_SECRET = "LwR4bT6bMNGVi43RXtKehreBzns7AEKBhhxvGMdmXbqwV"
english_words = set(nltk.corpus.words.words())
search_terms = sys.argv[1:]
class TweetListener(tweepy.StreamListener):
    def __init__(self, max_tweets=30):
        super().__init__()
        self.tweet_count = 0
        self.max_tweets = max_tweets
    def on_data(self, data):
        tweet_data = json.loads(data)
        with open("new_tweets.txt", "a", encoding='utf-8') as output_file:
            username = tweet_data["user"]["name"]
            verified = tweet_data["user"]["verified"]
            text = tweet_data.get("text", "")
            if "extended_tweet" in tweet_data:
                text = tweet_data["extended_tweet"].get('full_text', "")
            cleaned_text = re.sub(r"[^A-Za-z0-9_@./\s]", "", text)
            output_line = f'Username: {username}, Verified: {verified}, Text: {cleaned_text}\n'
            print(output_line, end='')
            output_file.write(output_line)
            self.tweet_count += 1
            if self.tweet_count >= self.max_tweets:
                print(f"{self.max_tweets} tweets fetched.")
                return False
    def on_error(self, status):
        print(f"Error: {status}")
if __name__ == "__main__":
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    search_query = " ".join(search_terms)
    print(f"Tracking: {search_query}")
    tweet_listener = TweetListener()
    twitter_stream = tweepy.Stream(auth, tweet_listener)
    twitter_stream.filter(languages=["en"], track=[search_query])