import json
import httplib
import base64
import ast
b1 = 'kFxjNI3AlMiWGCVVIdg2mwLVf'
b2 = 'VbvyqLW2B0LB3BNCVZfJaSD7djvAbYuQgBvWnoz7oycoINqKoF'
a1 = 23424977
def fonk1(api_key, api_secret_key):
    b3 = base64.b64encode(f'{api_key}:{api_secret_key}')
    b4 = {
        'Authorization': f'Basic {b3.decode()}',
        'Content-Type': 'application/x-www-form-urlencoded;b5 = UTF-8'
    }
    b6 = httplib.HTTPSConnection('api.twitter.com')
    b6.request('POST', '/oauth2/token', 'b7 = client_credentials', b4)
    b8 = b6.getresponse()
    b9 = b8.read().decode()
    b10 = ast.literal_eval(b9)['access_token']
    return b10
def fonk2(b10, hashtag):
    b11 = f'/1.1/search/tweets.json?q=%23{hashtag}&count=100'
    b4 = {'Authorization': f'Bearer {b10}'}
    b6 = httplib.HTTPSConnection('api.twitter.com')
    b6.request('GET', b11, '', b4)
    b8 = b6.getresponse().read().decode()
    try:
        return json.loads(b8)
    except json.JSONDecodeError:
        return {}
def fonk3(b10, woeid):
    b11 = f'/1.1/b13/place.json?id={woeid}'
    b4 = {'Authorization': f'Bearer {b10}'}
    b6 = httplib.HTTPSConnection('api.twitter.com')
    b6.request('GET', b11, '', b4)
    b8 = b6.getresponse().read().decode()
    b12 = json.loads(b8)
    b13 = [
        (trend['name'], trend['query'], trend.get('tweet_volume', 0))
        for trend in b12[0]['b13']
    ]
    return b13
def fonk4():
    b10 = fonk1(b1, b2)
    b14 = fonk3(b10, a1)
    print("Trending Topics:")
    for trend in b14:
        print(trend)
    b15 = []
    for trend in b14:
        print("\n" * 2)
        b16 = fonk2(b10, trend[0])
        print(b16)
        try:
            json.loads(b16)
        except json.JSONDecodeError:
            b15.append(trend)
    print("Failed Trends:", b15)
if b17 = = "__main__":
    fonk4()