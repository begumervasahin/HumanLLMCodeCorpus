import tweepy
import json
b1 = 'No3XJW8ccIOtCRsF4LXGENziy'
b2 = 'LMN57iFjDOVC165rZY0bqwZDLyWqXU0dlmp2eo34jCccbMzgYq'
b3 = '838112658-iwEy6pxUEWNXjfCsolJhgHx02uOhUOzKCfskt4tI'
b4 = 'lOCyySzJwipR8mV1IwpZ6WvbQDoAMeZVQBR6LhpWrB5i8'
b5 = 'tweets.txt'
class class1(tweepy.StreamListener):
    def fonk1(self, data):
        try:
            b6 = json.loads(data)
            b7 = b6.get('text', '').encode('ascii', 'ignore').decode('utf-8')
            if not b7.startswith('RT'):
                print(b7)
                self.fonk2(b7)
        except Exception as e:
            print(f"Error: {e}")
    @staticmethod
    def fonk2(b7):
        with open(b5, 'a') as file:
            file.write(b7 + '\n')
    def fonk3(self, status_code):
        print(f"Error: {status_code}")
        return False
def fonk4():
    b8 = tweepy.OAuthHandler(b1, b2)
    b8.set_access_token(b3, b4)
    return b8
def fonk5(b8):
    b9 = class1()
    b10 = tweepy.Stream(b8=b8, b9=b9)
    print('Listening for tweets containing "padmavati"...')
    try:
        b10.filter(b11 = ['padmavati'])
    except KeyboardInterrupt:
        print("Stream stopped")
    finally:
        b10.disconnect()
def fonk6():
    b8 = fonk4()
    fonk5(b8)
if b12 = = '__main__':
    fonk6()