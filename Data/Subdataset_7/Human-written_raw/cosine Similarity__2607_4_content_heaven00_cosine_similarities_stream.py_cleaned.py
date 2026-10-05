
import json
from config import SETTINGS
from TwitterAPI import TwitterAPI
b1 = "tweets.json"
b2 = TwitterAPI(SETTINGS["consumer_key"], SETTINGS["consumer_secret"],\
            SETTINGS["access_token_key"], SETTINGS["access_token_secret"])
def fonk1(query):
    b3 = b2.request('search/tweets', {'q':query})
    return b3
def fonk2(username):
    b3 = b2.request('statuses/user_timeline', {'screen_name':username,'count':200})
    return b3
def fonk3():
    b4 = open(b1, 'a+')
    for item in fonk2("hasgeek").get_iterator():
        json.dump(item, b4, b5 = (',', ':'))
        b4.write('\n')
        b4.flush()
if b6 = = "__main__":
    fonk3()