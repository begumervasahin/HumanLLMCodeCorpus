import tweepy
import json
CONSUMER_KEY = 'No3XJW8ccIOtCRsF4LXGENziy'
CONSUMER_SECRET = 'LMN57iFjDOVC165rZY0bqwZDLyWqXU0dlmp2eo34jCccbMzgYq'
ACCESS_TOKEN = '838112658-iwEy6pxUEWNXjfCsolJhgHx02uOhUOzKCfskt4tI'
ACCESS_TOKEN_SECRET = 'lOCyySzJwipR8mV1IwpZ6WvbQDoAMeZVQBR6LhpWrB5i8'
with open('tweets.txt', 'a') as file:
    class PrintListener(tweepy.StreamListener):
        def on_data(self, data):
            try:
                tweet = json.loads(data)
                tweet_text = tweet.get('text', '').encode('ascii', 'ignore').decode('utf-8')
                if not tweet_text.startswith('RT'):
                    print(tweet_text)
                    file.write(tweet_text + '\n')
            except Exception as e:
                print(f"Error: {e}")
        def on_error(self, status):
            print(f"Error: {status}")
    def main():
        try:
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
            listener = PrintListener()
            stream = tweepy.Stream(auth=auth, listener=listener)
            print('Listening for tweets containing "padmavati"...')
            stream.filter(track=['padmavati'])
        except KeyboardInterrupt:
            stream.disconnect()
            print("Stream stopped.")
    if __name__ == '__main__':
        main()