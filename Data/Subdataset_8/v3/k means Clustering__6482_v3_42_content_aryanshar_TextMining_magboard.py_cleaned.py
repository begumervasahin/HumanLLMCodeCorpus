import tweepy
import json
consumer_key = 'No3XJW8ccIOtCRsF4LXGENziy'
consumer_secret = 'LMN57iFjDOVC165rZY0bqwZDLyWqXU0dlmp2eo34jCccbMzgYq'
access_token = '838112658-iwEy6pxUEWNXjfCsolJhgHx02uOhUOzKCfskt4tI'
access_token_secret = 'lOCyySzJwipR8mV1IwpZ6WvbQDoAMeZVQBR6LhpWrB5i8'
file = open('tweets.txt', 'a')
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        try:
            tweet = json.loads(data)
            tweet_text = tweet.get('text', '').encode('ascii', 'ignore').decode('utf-8')
            if not tweet_text.startswith('RT'):
                print_and_write_tweet(tweet_text)
        except Exception as e:
            print_error(e)
    def on_error(self, status):
        print_error(status)
def print_and_write_tweet(tweet_text):
    print(tweet_text)
    file.write(tweet_text + '\n')
def print_error(error):
    print("Error:", error)
if __name__ == '__main__':
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        listener = PrintListener()
        stream = tweepy.Stream(auth, listener)
        print('Listening for tweets containing "padmavati"...')
        stream.filter(track=['padmavati'])
    except KeyboardInterrupt:
        file.close()
        stream.disconnect()