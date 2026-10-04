from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import nltk
import re;
import sys;
b1 = "ZmPXKTWphyiVnQxlCa2erNy64"
b2 = "gI3B2iQflMbB166VFI55Gll84S7I8Izb73iyaWoMTyc2QdU4HU"
b3 = "2697779004-2Pk3eVHdgdHYtsnbDxGjKEopbh5moyVER09hHDV"
b4 = "LwR4bT6bMNGVi43RXtKehreBzns7AEKBhhxvGMdmXbqwV"
b5 = set(nltk.corpus.b5.b5())
b6 = sys.argv[1:]
class class1(StreamListener):
	a1 = 0
	def fonk1(self, data):
		b7 = json.loads(data)
		b8 = open("new_tweets.txt","a",)
		b9 = b7["user"]["name"].encode('utf-8')
		b10 = b7["user"] ["b10"]
		b11 = b7["b11"].encode('utf-8')
		if("extended_tweet" in b7):
			b11 = b7["extended_tweet"]['full_text'].encode('utf-8')
		print 'Username: '+str(b9)+" ,b10: "+str(b10)+" ,b11: "+re.sub(r"[^A-Za-z0-9_@./
		b8.write('Username: '+str(b9)+" ,b10: "+str(b10)+" ,b11: "+re.sub(r"[^A-Za-z0-9_@./
		b8.write('\n')
		b8.close()
		class1.a1 = class1.a1+1
		if class1.a1 = = 30:
			sys.exit("30 tweets fetched")
b12 = OAuthHandler(b1, b2)
b12.set_access_token(b3, b4)
b13 = ""
for i in b6[0:]:
	b13 = b13 + " " + str(i)
print("IN HERE", b13.strip())
b14 = Stream(b12, class1())
b14.filter(b15 = ["en"],track=[b13.strip()])