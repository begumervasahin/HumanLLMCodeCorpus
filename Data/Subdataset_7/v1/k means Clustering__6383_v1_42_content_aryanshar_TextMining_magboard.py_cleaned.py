import tweepy
import json
b1 = 'No3XJW8ccIOtCRsF4LXGENziy'
b2 = 'LMN57iFjDOVC165rZY0bqwZDLyWqXU0dlmp2eo34jCccbMzgYq'
b3 = '838112658-iwEy6pxUEWNXjfCsolJhgHx02uOhUOzKCfskt4tI'
b4 = 'lOCyySzJwipR8mV1IwpZ6WvbQDoAMeZVQBR6LhpWrB5i8'
b5 = open('tweets.txt', 'a')
class class1(tweepy.StreamListener):
    def fonk1(self, data):
        try:
            b6 = json.loads(data)
            b7 = b6.get('text', '').encode('ascii', 'ignore').decode('utf-8')
            if not b7.startswith('RT'):
                print(b7)
                b5.write(b7 + '\n')
        except Exception as e:
            print("Error:", e)
    def fonk2(self, status):
        print("Error:", status)
if b8 = = '__main__':
    try:
        b9 = tweepy.OAuthHandler(b1, b2)
        b9.set_access_token(b3, b4)
        b10 = class1()
        b11 = tweepy.Stream(b9, b10)
        print('Listening for tweets containing "padmavati"...')
        b11.filter(b12 = ['padmavati'])
    except KeyboardInterrupt:
        b5.close()
        b11.disconnect()