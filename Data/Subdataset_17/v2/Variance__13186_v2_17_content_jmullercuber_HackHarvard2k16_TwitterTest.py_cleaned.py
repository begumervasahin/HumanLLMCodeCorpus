import requests
import base64
import json
API_KEY = 'kFxjNI3AlMiWGCVVIdg2mwLVf'
API_SECRET = 'VbvyqLW2B0LB3BNCVZfJaSD7djvAbYuQgBvWnoz7oycoINqKoF'
WOEID = 23424977
def get_bearer_token(api_key, api_secret):
    credentials = base64.b64encode(f'{api_key}:{api_secret}'.encode()).decode()
    headers = {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    response = requests.post(
        'https:
        headers=headers,
        data={'grant_type': 'client_credentials'}
    )
    response.raise_for_status()
    return response.json().get('access_token')
def get_tweets_by_hashtag(bearer_token, hashtag):
    url = f'https:
    headers = {'Authorization': f'Bearer {bearer_token}'}
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except json.JSONDecodeError:
        return {}
def get_trending_topics(bearer_token, woeid):
    url = f'https:
    headers = {'Authorization': f'Bearer {bearer_token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    trends_data = response.json()
    trends = [
        (trend['name'], trend['query'], trend.get('tweet_volume'))
        for trend in trends_data[0]['trends']
    ]
    return trends
def main():
    bearer_token = get_bearer_token(API_KEY, API_SECRET)
    trending_topics = get_trending_topics(bearer_token, WOEID)
    print("Trending Topics:")
    print(json.dumps(trending_topics, indent=2))
    failed_queries = []
    for topic in trending_topics:
        print(f"\nTrending Topic: {topic[0]}")
        print('-' * 40)
        tweets = get_tweets_by_hashtag(bearer_token, topic[0])
        print(json.dumps(tweets, indent=2))
        try:
            json.dumps(tweets)
        except json.JSONDecodeError:
            failed_queries.append(topic)
    if failed_queries:
        print("\nFailed to fetch tweets for the following topics:")
        print(json.dumps(failed_queries, indent=2))
if __name__ == "__main__":
    main()