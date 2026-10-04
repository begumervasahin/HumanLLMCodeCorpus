import json
import httplib
import urllib
import base64
import ast
b1 = 'kFxjNI3AlMiWGCVVIdg2mwLVf'
b2 = 'VbvyqLW2B0LB3BNCVZfJaSD7djvAbYuQgBvWnoz7oycoINqKoF'
a1 = 23424977
def fonk1(api_key, api_secret_key):
    b3 = base64.b64encode(f'{api_key}:{api_secret_key}')
    b4 = {
        'Authorization': f'Basic {b3}',
        'Content-Type': 'application/x-www-form-urlencoded;b5 = UTF-8'
    }
    b6 = httplib.HTTPSConnection('api.twitter.com')
    b6.request('POST', '/oauth2/token', 'b7 = client_credentials', b4)
    b8 = b6.getresponse()
    b9 = ast.literal_eval(b8.read())['access_token']
    return b9
def fonk2(b9, hashtag):
    b10 = f'/1.1/search/tweets.json?q=%23{hashtag}&count=100'
    b4 = {'Authorization': f'Bearer {b9}'}
    b6 = httplib.HTTPSConnection('api.twitter.com')
    b6.request('GET', b10, '', b4)
    b8 = b6.getresponse().read()
    try:
        return json.loads(b8)
    except json.JSONDecodeError:
        return {}
def fonk3(b9, woeid):
    b10 = f'/1.1/b12/place.json?id={woeid}'
    b4 = {'Authorization': f'Bearer {b9}'}
    b6 = httplib.HTTPSConnection('api.twitter.com')
    b6.request('GET', b10, '', b4)
    b8 = b6.getresponse().read()
    b11 = json.loads(b8)
    b12 = [
        (trend['name'], trend['query'], trend['tweet_volume'])
        for trend in b11[0]['b12']
    ]
    return b12
if b13 = = "__main__":
    b9 = fonk1(b1, b2)
    b14 = fonk3(b9, a1)
    print("Trending Topics:")
    for trend in b14:
        print(trend)
    b15 = []
    for trend in b14:
        print("\n" * 2)
        b16 = fonk2(b9, trend[0])
        print(b16)
        try:
            json.loads(b16)
        except json.JSONDecodeError:
            b15.append(trend)
    print("Failed Trends:", b15)