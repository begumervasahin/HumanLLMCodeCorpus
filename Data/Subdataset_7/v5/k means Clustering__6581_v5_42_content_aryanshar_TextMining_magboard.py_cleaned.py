import tweepy
import json
b1 = 'No3XJW8ccIOtCRsF4LXGENziy'
b2 = 'LMN57iFjDOVC165rZY0bqwZDLyWqXU0dlmp2eo34jCccbMzgYq'
b3 = '838112658-iwEy6pxUEWNXjfCsolJhgHx02uOhUOzKCfskt4tI'
b4 = 'lOCyySzJwipR8mV1IwpZ6WvbQDoAMeZVQBR6LhpWrB5i8'
with open('tweets.txt', 'a') as file:
    class class1(tweepy.StreamListener):
        def fonk1(self, data):
            b5 = json.loads(data)
            b6 = b5['text']
            b6 = b6.replace("RT", '')
            print(len(list_array))
            file.write(b6 + '\n')
        def fonk2(self, status):
            print(status)
    if b7 = = '__main__':
        b8 = class1()
        print('I will now print Tweets containing "Padmavati"! ==>')
        b9 = tweepy.OAuthHandler(b1, b2)
        b9.set_access_token(b3, b4)
        b10 = tweepy.Stream(b9, b8)
        b10.filter(b11 = ['padmavati'])