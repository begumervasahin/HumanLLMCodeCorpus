import requests
import base64
import json
b1 = 'kFxjNI3AlMiWGCVVIdg2mwLVf'
b2 = 'VbvyqLW2B0LB3BNCVZfJaSD7djvAbYuQgBvWnoz7oycoINqKoF'
a1 = 23424977
def fonk1(api_key, api_secret):
    b3 = base64.b64encode(f'{api_key}:{api_secret}'.encode()).decode()
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
    return b6.json().get('access_token')
def fonk2(b11, hashtag):
    b8 = f'https:
    b4 = {'Authorization': f'Bearer {b11}'}
    b6 = requests.get(b8, b4=b4)
    try:
        return b6.json()
    except json.JSONDecodeError:
        return {}
def fonk3(b11, woeid):
    b8 = f'https:
    b4 = {'Authorization': f'Bearer {b11}'}
    b6 = requests.get(b8, b4=b4)
    b6.raise_for_status()
    b9 = b6.json()
    b10 = [
        (trend['name'], trend['query'], trend.get('tweet_volume'))
        for trend in b9[0]['b10']
    ]
    return b10
def fonk4():
    b11 = fonk1(b1, b2)
    b12 = fonk3(b11, a1)
    print("Trending Topics:")
    print(json.dumps(b12, b13 = 2))
    b14 = []
    for topic in b12:
        print(f"\nTrending Topic: {topic[0]}")
        print('-' * 40)
        b15 = fonk2(b11, topic[0])
        print(json.dumps(b15, b13 = 2))
        try:
            json.dumps(b15)
        except json.JSONDecodeError:
            b14.append(topic)
    if b14:
        print("\nFailed to fetch b15 for the following topics:")
        print(json.dumps(b14, b13 = 2))
if b16 = = "__main__":
    fonk4()