from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import nltk
import re;
import sys;
ckey="ZmPXKTWphyiVnQxlCa2erNy64"
csecret="gI3B2iQflMbB166VFI55Gll84S7I8Izb73iyaWoMTyc2QdU4HU"
atoken="2697779004-2Pk3eVHdgdHYtsnbDxGjKEopbh5moyVER09hHDV"
asecret="LwR4bT6bMNGVi43RXtKehreBzns7AEKBhhxvGMdmXbqwV"
words = set(nltk.corpus.words.words())
args = sys.argv[1:]
class listener(StreamListener):
	c = 0
	def on_data(self, data):
		all_data = json.loads(data)
		output = open("new_tweets.txt","a",)
		userName = all_data["user"]["name"].encode('utf-8')
		verified = all_data["user"] ["verified"]
		text = all_data["text"].encode('utf-8')
		if("extended_tweet" in all_data):
			text = all_data["extended_tweet"]['full_text'].encode('utf-8')
		print 'Username: '+str(userName)+" ,verified: "+str(verified)+" ,text: "+re.sub(r"[^A-Za-z0-9_@./
		output.write('Username: '+str(userName)+" ,verified: "+str(verified)+" ,text: "+re.sub(r"[^A-Za-z0-9_@./
		output.write('\n')
		output.close()
		listener.c = listener.c+1
		if listener.c == 30:
			sys.exit("30 tweets fetched")
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
queryString = ""
for i in args[0:]:
	queryString = queryString + " " + str(i)
print("IN HERE", queryString.strip())
twitterStream = Stream(auth, listener())
twitterStream.filter(languages=["en"],track=[queryString.strip()])