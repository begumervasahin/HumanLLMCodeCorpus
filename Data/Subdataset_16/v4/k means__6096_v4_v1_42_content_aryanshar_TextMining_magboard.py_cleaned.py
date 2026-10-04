import tweepy
import json
b1 = 'No3XJW8ccIOtCRsF4LXGENziy'
b2 = 'LMN57iFjDOVC165rZY0bqwZDLyWqXU0dlmp2eo34jCccbMzgYq'
b3 = '838112658-iwEy6pxUEWNXjfCsolJhgHx02uOhUOzKCfskt4tI'
b4 = 'lOCyySzJwipR8mV1IwpZ6WvbQDoAMeZVQBR6LhpWrB5i8'
with open('tweets.txt', 'a') as file:
    class class1(tweepy.StreamListener):
        def fonk1(self, data):
            try:
                b5 = json.loads(data)
                b6 = b5.get('text', '').encode('ascii', 'ignore').decode('utf-8')
                if not b6.startswith('RT'):
                    print(b6)
                    file.write(b6 + '\n')
            except Exception as e:
                print("Error:", e)
        def fonk2(self, status):
            print("Error:", status)
    if b7 = = '__main__':
        try:
            b8 = tweepy.OAuthHandler(b1, b2)
            b8.set_access_token(b3, b4)
            b9 = class1()
            b10 = tweepy.Stream(b8, b9)
            print('Listening for tweets containing "padmavati"...')
            b10.filter(b11 = ['padmavati'])
        except KeyboardInterrupt:
            b10.disconnect()