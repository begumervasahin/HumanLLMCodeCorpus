import tweepy
import json
CONSUMER_KEY = 'No3XJW8ccIOtCRsF4LXGENziy'
CONSUMER_SECRET = 'LMN57iFjDOVC165rZY0bqwZDLyWqXU0dlmp2eo34jCccbMzgYq'
ACCESS_TOKEN = '838112658-iwEy6pxUEWNXjfCsolJhgHx02uOhUOzKCfskt4tI'
ACCESS_TOKEN_SECRET = 'lOCyySzJwipR8mV1IwpZ6WvbQDoAMeZVQBR6LhpWrB5i8'
with open('tweets.txt', 'a') as file:
    class PrintListener(tweepy.StreamListener):
        def on_data(self, data):
            tweet = json.loads(data)
            tweet_text = tweet['text']
            tweet_text = tweet_text.replace("RT", '')
            print(len(list_array))
            file.write(tweet_text + '\n')
        def on_error(self, status):
            print(status)
    if __name__ == '__main__':
        listener = PrintListener()
        print('I will now print Tweets containing "Padmavati"! ==>')
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = tweepy.Stream(auth, listener)
        stream.filter(track=['padmavati'])