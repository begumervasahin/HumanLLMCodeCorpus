import tweepy
import json
CONSUMER_KEY = 'No3XJW8ccIOtCRsF4LXGENziy'
CONSUMER_SECRET = 'LMN57iFjDOVC165rZY0bqwZDLyWqXU0dlmp2eo34jCccbMzgYq'
ACCESS_TOKEN = '838112658-iwEy6pxUEWNXjfCsolJhgHx02uOhUOzKCfskt4tI'
ACCESS_TOKEN_SECRET = 'lOCyySzJwipR8mV1IwpZ6WvbQDoAMeZVQBR6LhpWrB5i8'
TWEET_FILE = 'tweets.txt'
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        try:
            tweet = json.loads(data)
            tweet_text = tweet.get('text', '').encode('ascii', 'ignore').decode('utf-8')
            if not tweet_text.startswith('RT'):
                print(tweet_text)
                self.write_to_file(tweet_text)
        except Exception as e:
            print(f"Error: {e}")
    @staticmethod
    def write_to_file(tweet_text):
        with open(TWEET_FILE, 'a') as file:
            file.write(tweet_text + '\n')
    def on_error(self, status_code):
        print(f"Error: {status_code}")
        return False
def authenticate_twitter_app():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return auth
def start_stream(auth):
    listener = PrintListener()
    stream = tweepy.Stream(auth=auth, listener=listener)
    print('Listening for tweets containing "padmavati"...')
    try:
        stream.filter(track=['padmavati'])
    except KeyboardInterrupt:
        print("Stream stopped")
    finally:
        stream.disconnect()
def main():
    auth = authenticate_twitter_app()
    start_stream(auth)
if __name__ == '__main__':
    main()