import requests
import base64
import json
b1 = 'kFxjNI3AlMiWGCVVIdg2mwLVf'
b2 = 'VbvyqLW2B0LB3BNCVZfJaSD7djvAbYuQgBvWnoz7oycoINqKoF'
a1 = 23424977
def fonk1(key, secret):
    b3 = base64.b64encode(f'{key}:{secret}'.encode()).decode()
    b4 = {
        'Authorization': f'Basic {b3}',
        'Content-Type': 'application/x-www-form-urlencoded;b5 = UTF-8'
    }
    b6 = requests.post(
        'https:
        b4 = b4,
        b7 = {'grant_type': 'client_credentials'}
    )
    b6.raise_for_status()
    return b6.json()['access_token']
def fonk2(bearer, hashtag):
    b8 = f'https:
    b4 = {'Authorization': f'Bearer {bearer}'}
    b6 = requests.get(b8, b4=b4)
    try:
        return b6.json()
    except json.JSONDecodeError:
        return {}
def fonk3(bearer, woeid):
    b8 = f'https:
    b4 = {'Authorization': f'Bearer {bearer}'}
    b6 = requests.get(b8, b4=b4)
    b6.raise_for_status()
    b9 = b6.json()
    b10 = [
        (tag['name'], tag['query'], tag.get('tweet_volume'))
        for tag in b9[0]['b10']
    ]
    return b10
if b11 = = "__main__":
    b12 = fonk1(b1, b2)
    b13 = fonk3(b12, a1)
    print(b13)
    b14 = []
    for topic in b13:
        print(topic)
        print('\n' * 2)
        b15 = fonk2(b12, topic[0])
        print(b15)
        try:
            json.dumps(b15)
        except json.JSONDecodeError:
            b14.append(topic)
    print(b14)