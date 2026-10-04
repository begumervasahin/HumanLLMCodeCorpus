import json
import httplib
import urllib
import base64
import ast
API_KEY = 'kFxjNI3AlMiWGCVVIdg2mwLVf'
API_SECRET_KEY = 'VbvyqLW2B0LB3BNCVZfJaSD7djvAbYuQgBvWnoz7oycoINqKoF'
WOEID = 23424977
def get_bearer_token(api_key, api_secret_key):
    credentials = base64.b64encode(f'{api_key}:{api_secret_key}')
    headers = {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    conn = httplib.HTTPSConnection('api.twitter.com')
    conn.request('POST', '/oauth2/token', 'grant_type=client_credentials', headers)
    response = conn.getresponse()
    bearer_token = ast.literal_eval(response.read())['access_token']
    return bearer_token
def get_results(bearer_token, hashtag):
    url = f'/1.1/search/tweets.json?q=%23{hashtag}&count=100'
    headers = {'Authorization': f'Bearer {bearer_token}'}
    conn = httplib.HTTPSConnection('api.twitter.com')
    conn.request('GET', url, '', headers)
    response = conn.getresponse().read()
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {}
def get_trending_topics(bearer_token, woeid):
    url = f'/1.1/trends/place.json?id={woeid}'
    headers = {'Authorization': f'Bearer {bearer_token}'}
    conn = httplib.HTTPSConnection('api.twitter.com')
    conn.request('GET', url, '', headers)
    response = conn.getresponse().read()
    tweet_data = json.loads(response)
    trends = [
        (trend['name'], trend['query'], trend['tweet_volume'])
        for trend in tweet_data[0]['trends']
    ]
    return trends
if __name__ == "__main__":
    bearer_token = get_bearer_token(API_KEY, API_SECRET_KEY)
    trending_topics = get_trending_topics(bearer_token, WOEID)
    print("Trending Topics:")
    for trend in trending_topics:
        print(trend)
    failed_trends = []
    for trend in trending_topics:
        print("\n" * 2)
        results = get_results(bearer_token, trend[0])
        print(results)
        try:
            json.loads(results)
        except json.JSONDecodeError:
            failed_trends.append(trend)
    print("Failed Trends:", failed_trends)