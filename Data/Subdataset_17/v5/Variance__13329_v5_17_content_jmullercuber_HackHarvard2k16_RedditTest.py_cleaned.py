import json
import http.client
import string
def filter_printable_text(text):
    return ''.join(filter(lambda x: x in string.printable, text))
def recurse_comments(comment):
    comments_text = []
    body = filter_printable_text(comment['data']['body'])
    comments_text.append(body)
    if comment['data']['replies']:
        for reply in comment['data']['replies']['data']['children']:
            if reply['kind'] != 'more':
                comments_text.extend(recurse_comments(reply))
    return comments_text
def fetch_json_response(connection, url):
    connection.request("GET", url)
    response = connection.getresponse()
    return json.loads(response.read())
def extract_comments_from_post(post_data):
    top_level_posts = post_data[1]['data']['children']
    all_comments = []
    for post in top_level_posts:
        if 'body' in post['data']:
            all_comments.extend(recurse_comments(post))
    return all_comments
def prepare_cognitive_request_body(comments):
    return {
        'stop_words': [],
        'topicsToExclude': [],
        'documents': [{'id': str(i), 'text': comment} for i, comment in enumerate(comments)]
    }
def main():
    reddit_conn = http.client.HTTPSConnection('www.reddit.com')
    subreddit_data = fetch_json_response(reddit_conn, "/r/worldnews/hot/.json")
    first_post_permalink = subreddit_data['data']['children'][0]['data']['permalink']
    post_data = fetch_json_response(reddit_conn, f"{first_post_permalink}.json")
    all_comments = extract_comments_from_post(post_data)
    print(f"Total comments extracted: {len(all_comments)}")
    cognitive_body = prepare_cognitive_request_body(all_comments)
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
    }
    cognitive_conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    cognitive_conn.request("POST", "/text/analytics/v2.0/topics", json.dumps(cognitive_body), headers)
    response = cognitive_conn.getresponse()
    response_headers = response.getheaders()
    response_data = json.loads(response.read())
    print(response_headers)
    print(response_data)
    cognitive_conn.close()
    reddit_conn.close()
if __name__ == "__main__":
    main()