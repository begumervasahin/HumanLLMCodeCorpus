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
conn = http.client.HTTPSConnection('www.reddit.com')
conn.request("GET", "/r/worldnews/hot/.json")
response = conn.getresponse()
sr_data = json.loads(response.read().decode())
post_permalink = sr_data['data']['children'][0]['data']['permalink']
conn.request("GET", f"{post_permalink}.json")
response = conn.getresponse()
p_data = json.loads(response.read().decode())
tl_posts = p_data[1]['data']['children']
all_comments = []
for post in tl_posts:
    if 'body' in post['data']:
        all_comments.extend(recurse_comments(post))
print(len(all_comments))
c_body = {
    'stop_words': [],
    'topicsToExclude': [],
    'documents': [{'id': str(i), 'text': reply} for i, reply in enumerate(all_comments)]
}
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
conn2 = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
conn2.request("POST", "/text/analytics/v2.0/topics", json.dumps(c_body), headers)
response = conn2.getresponse()
print(response.getheaders())
data = json.loads(response.read().decode())
print(data)
conn2.close()
conn.close()