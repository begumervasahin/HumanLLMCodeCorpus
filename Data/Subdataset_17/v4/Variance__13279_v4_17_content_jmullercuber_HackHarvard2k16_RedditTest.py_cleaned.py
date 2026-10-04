import json
import http.client
import string
def recurse_comments(comment):
    text = []
    body = ''.join(filter(lambda x: x in string.printable, comment['data']['body']))
    text.append(body)
    if comment['data']['replies']:
        for reply in comment['data']['replies']['data']['children']:
            if reply['kind'] != 'more':
                text.extend(recurse_comments(reply))
    return text
conn = http.client.HTTPSConnection('www.reddit.com')
conn.request("GET", "/r/worldnews/hot/.json")
response = conn.getresponse()
subreddit_data = json.loads(response.read())
first_post_permalink = subreddit_data['data']['children'][0]['data']['permalink']
conn.request("GET", f"{first_post_permalink}.json")
response = conn.getresponse()
post_data = json.loads(response.read())
top_level_posts = post_data[1]['data']['children']
all_comments = []
for post in top_level_posts:
    if 'body' in post['data']:
        all_comments.extend(recurse_comments(post))
print(f"Total comments extracted: {len(all_comments)}")
cognitive_body = {
    'stop_words': [],
    'topicsToExclude': [],
    'documents': []
}
for count, reply in enumerate(all_comments):
    cognitive_body['documents'].append({
        'id': str(count),
        'text': reply
    })
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
conn2 = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
conn2.request("POST", "/text/analytics/v2.0/topics", json.dumps(cognitive_body), headers)
response = conn2.getresponse()
response_headers = response.getheaders()
response_data = json.loads(response.read())
print(response_headers)
print(response_data)
conn2.close()
conn.close()