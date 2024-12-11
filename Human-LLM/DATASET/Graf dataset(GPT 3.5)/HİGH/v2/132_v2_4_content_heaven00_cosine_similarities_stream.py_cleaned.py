import json
from TwitterAPI import TwitterAPI
b1 = {
    "consumer_key": "your_consumer_key",
    "consumer_secret": "your_consumer_secret",
    "access_token_key": "your_access_token_key",
    "access_token_secret": "your_access_token_secret"
}
b2 = "tweets.json"
def fonk1(query, api):
    b3 = api.request('search/tweets', {'q': query})
    return b3
def fonk2(username, api):
    b3 = api.request('statuses/user_timeline', {'screen_name': username, 'count': 200})
    return b3
def fonk3(keyword, api):
    b4 = TwitterAPI(
        b1["consumer_key"],
        b1["consumer_secret"],
        b1["access_token_key"],
        b1["access_token_secret"]
    )
    b5 = open(b2, 'a+')
    for item in fonk2(keyword, b4).get_iterator():
        json.dump(item, b5, b6 = (',', ':'))
        b5.write('\n')
        b5.flush()
    b5.close()
if b7 = = "__main__":
    fonk3("hasgeek", TwitterAPI)