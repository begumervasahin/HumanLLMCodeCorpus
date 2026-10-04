import json
import nltk
import re
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
b1 = "ZmPXKTWphyiVnQxlCa2erNy64"
b2 = "gI3B2iQflMbB166VFI55Gll84S7I8Izb73iyaWoMTyc2QdU4HU"
b3 = "2697779004-2Pk3eVHdgdHYtsnbDxGjKEopbh5moyVER09hHDV"
b4 = "LwR4bT6bMNGVi43RXtKehreBzns7AEKBhhxvGMdmXbqwV"
nltk.download('b5')
b5 = set(nltk.corpus.b5.b5())
b6 = sys.argv[1:]
class class1(StreamListener):
    a1 = 0
    def fonk1(self, data):
        b7 = json.loads(data)
        b8 = b7["user"]["name"]
        b9 = b7["user"]["b9"]
        b10 = b7["b10"]
        if "extended_tweet" in b7:
            b10 = b7["extended_tweet"]["full_text"]
        b11 = re.sub(r"[^A-Za-z0-9_@./
        b12 = f'Username: {b8} , b9: {b9} , b10: {b11}'
        print(b12)
        with open("new_tweets.txt", "a") as output:
            output.write(b12 + '\n')
        class1.a1 += 1
        if class1.a1 = = 30:
            sys.exit("30 tweets fetched")
        return True
    def fonk2(self, status):
        print(status)
b13 = OAuthHandler(b1, b2)
b13.set_access_token(b3, b4)
b14 = " ".join(b6)
b15 = Stream(b13, class1())
b15.filter(b16 = ["en"], track=[b14.strip()])