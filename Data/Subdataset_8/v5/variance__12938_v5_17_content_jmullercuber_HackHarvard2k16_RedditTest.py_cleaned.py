import json
import httplib
import string
def extract_comments(comment):
    comments = []
    body = filter(lambda x: x in string.printable, comment['data']['body'])
    comments.append(body)
    if 'replies' in comment['data'] and comment['data']['replies'] != '':
        for reply in comment['data']['replies']['data']['children']:
            if reply['kind'] != 'more':
                comments.extend(extract_comments(reply))
    return comments
def get_reddit_data(url):
    conn = httplib.HTTPSConnection('www.reddit.com')
    conn.request("GET", url)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return json.loads(data)
sr_data = get_reddit_data("/r/worldnews/hot/.json")
top_post_permalink = sr_data['data']['children'][0]['data']['permalink']
p_data = get_reddit_data(top_post_permalink + '.json')
tl_posts = p_data[1]['data']['children']
all_comments = []
for post in tl_posts:
    if 'body' in post['data']:
        all_comments.extend(extract_comments(post))
print("Total Comments:", len(all_comments))
documents = []
for idx, comment in enumerate(all_comments):
    documents.append({'id': str(idx), 'text': comment})
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
conn2 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
conn2.request("POST", "/text/analytics/v2.0/topics", json.dumps({'documents': documents}), headers)
response = conn2.getresponse()
data = response.read()
print("API Response:", data)
conn2.close()