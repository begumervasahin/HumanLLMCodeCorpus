import json
import httplib
import string
def extract_comments(comment):
    text = []
    body = filter(lambda x: x in string.printable, comment['data']['body'])
    text.append(body)
    if not comment['data']['replies'] == '':
        for reply in comment['data']['replies']['data']['children']:
            if not reply['kind'] == 'more':
                text.extend(extract_comments(reply))
    return text
conn = httplib.HTTPSConnection('www.reddit.com')
conn.request("GET", "/r/worldnews/hot/.json")
response = conn.getresponse()
sr_data = response.read()
sr_data = json.loads(sr_data)
conn.request("GET", sr_data['data']['children'][0]['data']['permalink'] + '.json')
response = conn.getresponse()
p_data = response.read()
p_data = json.loads(p_data)
tl_posts = p_data[1]['data']['children']
all_comments = []
for post in tl_posts:
    if 'body' in post['data']:
        all_comments.extend(extract_comments(post))
print(len(all_comments))
c_body = {
    'stop_words': [],
    'topicsToExclude': [],
    'documents': []
}
count = 0
for reply in all_comments:
    d = {
        'id': str(count),
        'text': reply
    }
    c_body['documents'].append(d)
    count += 1
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
conn2 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
conn2.request("POST", "/text/analytics/v2.0/topics", json.dumps(c_body), headers)
response = conn2.getresponse()
data = response.getheaders()
print(data)
data = json.loads(data)
conn2.close()
conn.close()