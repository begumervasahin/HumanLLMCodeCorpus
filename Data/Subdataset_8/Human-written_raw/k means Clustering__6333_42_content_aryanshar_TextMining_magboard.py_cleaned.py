import tweepy
import json
import re
consumer_key = 'No3XJW8ccIOtCRsF4LXGENziy'
consumer_secret = 'LMN57iFjDOVC165rZY0bqwZDLyWqXU0dlmp2eo34jCccbMzgYq'
access_token = '838112658-iwEy6pxUEWNXjfCsolJhgHx02uOhUOzKCfskt4tI'
access_token_secret = 'lOCyySzJwipR8mV1IwpZ6WvbQDoAMeZVQBR6LhpWrB5i8'
list_array =[]
file = open('tweets.txt', 'a')
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        tweet_filter = str(tweet['text'].encode('ascii', 'ignore'))
        tweet_text = tweet_filter.replace("RT", '')
        list_array.append(tweet_filter)
        print(len(list_array))
        file.write(tweet_text+'\n')
    def on_error(self, status):
        print(status)
if __name__ == '__main__':
    listener = PrintListener()
    print('I will now print Tweets containing "Padmavati"! ==>')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['padmavati', '