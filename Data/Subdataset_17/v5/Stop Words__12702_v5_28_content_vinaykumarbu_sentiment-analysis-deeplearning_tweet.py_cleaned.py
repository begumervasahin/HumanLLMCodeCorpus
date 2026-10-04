import json
import nltk
import re
import sys
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
CKEY = "ZmPXKTWphyiVnQxlCa2erNy64"
CSECRET = "gI3B2iQflMbB166VFI55Gll84S7I8Izb73iyaWoMTyc2QdU4HU"
ATOKEN = "2697779004-2Pk3eVHdgdHYtsnbDxGjKEopbh5moyVER09hHDV"
ASECRET = "LwR4bT6bMNGVi43RXtKehreBzns7AEKBhhxvGMdmXbqwV"
WORDS = set(nltk.corpus.words.words())
class TweetListener(StreamListener):
    def __init__(self, tweet_limit=30):
        super().__init__()
        self.tweet_count = 0
        self.tweet_limit = tweet_limit
    def on_data(self, data):
        try:
            all_data = json.loads(data)
            user_name = all_data["user"]["name"]
            verified = all_data["user"]["verified"]
            text = all_data.get("extended_tweet", {}).get("full_text", all_data["text"])
            clean_text = re.sub(r"[^A-Za-z0-9_@./
            with open("new_tweets.txt", "a") as output:
                output.write(f'Username: {user_name}, verified: {verified}, text: {clean_text}\n')
            self.tweet_count += 1
            if self.tweet_count >= self.tweet_limit:
                print(f"Fetched {self.tweet_limit} tweets. Exiting.")
                return False
            return True
        except Exception as e:
            print(f"Error on_data: {str(e)}")
            return True
def authenticate_twitter_app():
    auth = OAuthHandler(CKEY, CSECRET)
    auth.set_access_token(ATOKEN, ASECRET)
    return auth
def main():
    auth = authenticate_twitter_app()
    query_string = " ".join(sys.argv[1:]).strip()
    print("Query String:", query_string)
    twitter_stream = Stream(auth, TweetListener())
    twitter_stream.filter(languages=["en"], track=[query_string])
if __name__ == "__main__":
    main()