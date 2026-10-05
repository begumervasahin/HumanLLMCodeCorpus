import tweepy
import json
import re
b1 = 'No3XJW8ccIOtCRsF4LXGENziy'
b2 = 'LMN57iFjDOVC165rZY0bqwZDLyWqXU0dlmp2eo34jCccbMzgYq'
b3 = '838112658-iwEy6pxUEWNXjfCsolJhgHx02uOhUOzKCfskt4tI'
b4 = 'lOCyySzJwipR8mV1IwpZ6WvbQDoAMeZVQBR6LhpWrB5i8'
b5 = []
b6 = open('tweets.txt', 'a')
class class1(tweepy.StreamListener):
    def fonk1(self, data):
        b7 = json.loads(data)
        b8 = str(b7['text'].encode('ascii', 'ignore'))
        b9 = b8.replace("RT", '')
        b5.append(b8)
        print(len(b5))
        b6.write(b9+'\n')
    def fonk2(self, status):
        print(status)
if b10 = = '__main__':
    b11 = class1()
    print('I will now print Tweets containing "Padmavati"! ==>')
    b12 = tweepy.OAuthHandler(b1, b2)
    b12.set_access_token(b3, b4)
    b13 = tweepy.Stream(b12, b11)
    b13.filter(b14 = ['padmavati', '