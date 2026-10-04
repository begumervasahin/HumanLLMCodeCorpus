import json
import nltk
import re
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
ckey = "ZmPXKTWphyiVnQxlCa2erNy64"
csecret = "gI3B2iQflMbB166VFI55Gll84S7I8Izb73iyaWoMTyc2QdU4HU"
atoken = "2697779004-2Pk3eVHdgdHYtsnbDxGjKEopbh5moyVER09hHDV"
asecret = "LwR4bT6bMNGVi43RXtKehreBzns7AEKBhhxvGMdmXbqwV"
nltk.download('words')
words = set(nltk.corpus.words.words())
args = sys.argv[1:]
class Listener(StreamListener):
    count = 0
    def on_data(self, data):
        all_data = json.loads(data)
        user_name = all_data["user"]["name"]
        verified = all_data["user"]["verified"]
        text = all_data["text"]
        if "extended_tweet" in all_data:
            text = all_data["extended_tweet"]["full_text"]
        cleaned_text = re.sub(r"[^A-Za-z0-9_@./
        output_line = f'Username: {user_name} , verified: {verified} , text: {cleaned_text}'
        print(output_line)
        with open("new_tweets.txt", "a") as output:
            output.write(output_line + '\n')
        Listener.count += 1
        if Listener.count == 30:
            sys.exit("30 tweets fetched")
        return True
    def on_error(self, status):
        print(status)
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
query_string = " ".join(args)
twitter_stream = Stream(auth, Listener())
twitter_stream.filter(languages=["en"], track=[query_string.strip()])