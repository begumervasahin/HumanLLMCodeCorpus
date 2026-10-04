import json
import http.client
import string
def recurse_comments(comment):
    text = []
    body = ''.join(filter(lambda x: x in string.printable, comment['data']['body']))
    text.append(body)
    if comment['data']['replies'] != '':
        for reply in comment['data']['replies']['data']['children']:
            if reply['kind'] != 'more':
                text.extend(recurse_comments(reply))
    return text
def fetch_reddit_data(subreddit):
    conn = http.client.HTTPSConnection('www.reddit.com')
    conn.request("GET", f"/r/{subreddit}/hot/.json")
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    conn.close()
    return data
def fetch_post_comments(permalink):
    conn = http.client.HTTPSConnection('www.reddit.com')
    conn.request("GET", f"{permalink}.json")
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    conn.close()
    return data
def prepare_api_request_body(comments):
    documents = [{'id': str(i), 'text': comment} for i, comment in enumerate(comments)]
    return {
        'stop_words': [],
        'topicsToExclude': [],
        'documents': documents
    }
def analyze_topics(api_key, request_body):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': api_key,
    }
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/topics", json.dumps(request_body), headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    conn.close()
    return data
def main():
    subreddit = "worldnews"
    api_key = 'b3f5d9f8d81046598dedc07a7541e2c9'
    sr_data = fetch_reddit_data(subreddit)
    post_permalink = sr_data['data']['children'][0]['data']['permalink']
    p_data = fetch_post_comments(post_permalink)
    tl_posts = p_data[1]['data']['children']
    all_comments = []
    for post in tl_posts:
        if 'body' in post['data']:
            all_comments.extend(recurse_comments(post))
    print(f"Total comments collected: {len(all_comments)}")
    request_body = prepare_api_request_body(all_comments)
    response_data = analyze_topics(api_key, request_body)
    print(json.dumps(response_data, indent=4))
if __name__ == "__main__":
    main()