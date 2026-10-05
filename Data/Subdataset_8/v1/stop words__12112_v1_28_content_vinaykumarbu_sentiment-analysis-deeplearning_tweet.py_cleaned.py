import tweepy
import json
import nltk
import re
import sys
ckey = "ZmPXKTWphyiVnQxlCa2erNy64"
csecret = "gI3B2iQflMbB166VFI55Gll84S7I8Izb73iyaWoMTyc2QdU4HU"
atoken = "2697779004-2Pk3eVHdgdHYtsnbDxGjKEopbh5moyVER09hHDV"
asecret = "LwR4bT6bMNGVi43RXtKehreBzns7AEKBhhxvGMdmXbqwV"
words = set(nltk.corpus.words.words())
args = sys.argv[1:]
class TweetListener(tweepy.StreamListener):
    def __init__(self, max_tweets=30):
        super(TweetListener, self).__init__()
        self.counter = 0
        self.max_tweets = max_tweets
    def on_data(self, data):
        all_data = json.loads(data)
        with open("new_tweets.txt", "a", encoding='utf-8') as output:
            userName = all_data["user"]["name"]
            verified = all_data["user"]["verified"]
            text = all_data.get("text", "")
            if "extended_tweet" in all_data:
                text = all_data["extended_tweet"].get('full_text', "")
            cleaned_text = re.sub(r"[^A-Za-z0-9_@./\s]", "", text)
            output_line = f'Username: {userName}, Verified: {verified}, Text: {cleaned_text}\n'
            print(output_line, end='')
            output.write(output_line)
            self.counter += 1
            if self.counter >= self.max_tweets:
                print(f"{self.max_tweets} tweets fetched.")
                return False
    def on_error(self, status):
        print(f"Error: {status}")
if __name__ == "__main__":
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    queryString = " ".join(args)
    print(f"Tracking: {queryString}")
    twitterStream = tweepy.Stream(auth, TweetListener())
    twitterStream.filter(languages=["en"], track=[queryString])