import tweepy
import json
b1 = 'No3XJW8ccIOtCRsF4LXGENziy'
b2 = 'LMN57iFjDOVC165rZY0bqwZDLyWqXU0dlmp2eo34jCccbMzgYq'
b3 = '838112658-iwEy6pxUEWNXjfCsolJhgHx02uOhUOzKCfskt4tI'
b4 = 'lOCyySzJwipR8mV1IwpZ6WvbQDoAMeZVQBR6LhpWrB5i8'
b5 = open('tweets.txt', 'a')
class class1(tweepy.StreamListener):
    def fonk1(self, data):
        b6 = json.loads(data)
        b7 = b6['text']
        b7 = b7.replace("RT", '')
        list_array.append(b7)
        print(len(list_array))
        b5.write(b7 + '\n')
    def fonk2(self, status):
        print(status)
if b8 = = '__main__':
    b9 = class1()
    print('I will now print Tweets containing "Padmavati"! ==>')
    b10 = tweepy.OAuthHandler(b1, b2)
    b10.set_access_token(b3, b4)
    b11 = tweepy.Stream(b10, b9)
    b11.filter(b12 = ['padmavati'])