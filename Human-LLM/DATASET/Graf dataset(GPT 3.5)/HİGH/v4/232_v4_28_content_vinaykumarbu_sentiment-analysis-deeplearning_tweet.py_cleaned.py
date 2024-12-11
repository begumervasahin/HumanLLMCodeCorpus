import json
import re
import sys
import nltk
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
b1 = "YOUR_CONSUMER_KEY"
b2 = "YOUR_CONSUMER_SECRET"
b3 = "YOUR_ACCESS_TOKEN"
b4 = "YOUR_ACCESS_SECRET"
nltk.download('b5')
b5 = set(nltk.corpus.b5.b5())
class class1(StreamListener):
    a1 = 0
    def fonk1(self, data):
        b6 = json.loads(data)
        with open("new_tweets.txt", "a") as output:
            b7 = b6["user"]["name"].encode('utf-8')
            b8 = b6["user"]["b8"]
            b9 = b6["text"].encode('utf-8')
            if "extended_tweet" in b6:
                b9 = b6["extended_tweet"]["full_text"].encode('utf-8')
            b9 = re.sub(r"[^A-Za-z0-9_@./]", "", b9)
            print(f'Username: {b7}, Verified: {b8}, Text: {b9}')
            output.write(f'Username: {b7}, Verified: {b8}, Text: {b9}\n')
            class1.a1 += 1
            if class1.a1 = = 30:
                sys.exit("30 tweets fetched")
b10 = OAuthHandler(b1, b2)
b10.set_access_token(b3, b4)
b11 = " ".join(sys.argv[1:])
print("Query String:", b11)
b12 = Stream(b10, class1())
b12.filter(b13 = ["en"], track=[b11])