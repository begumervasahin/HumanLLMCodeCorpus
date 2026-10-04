import json
import http.client
import string
def fonk1(comment):
    b1 = []
    b2 = ''.join(filter(lambda x: x in string.printable, comment['data']['b2']))
    b1.append(b2)
    if comment['data']['replies']:
        for reply in comment['data']['replies']['data']['children']:
            if reply['kind'] != 'more':
                b1.extend(fonk1(reply))
    return b1
b3 = http.client.HTTPSConnection('www.reddit.com')
b3.request("GET", "/r/worldnews/hot/.json")
b4 = b3.getresponse()
b5 = json.loads(b4.read())
b6 = b5['data']['children'][0]['data']['permalink']
b3.request("GET", f"{b6}.json")
b4 = b3.getresponse()
b7 = json.loads(b4.read())
b8 = b7[1]['data']['children']
b9 = []
for post in b8:
    if 'b2' in post['data']:
        b9.extend(fonk1(post))
print(f"Total comments extracted: {len(b9)}")
b10 = {
    'stop_words': [],
    'topicsToExclude': [],
    'documents': []
}
for count, reply in enumerate(b9):
    b10['documents'].append({
        'id': str(count),
        'b1': reply
    })
b11 = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
b12 = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
b12.request("POST", "/b1/analytics/v2.0/topics", json.dumps(b10), b11)
b4 = b12.getresponse()
b13 = b4.getheaders()
b14 = json.loads(b4.read())
print(b13)
print(b14)
b12.close()
b3.close()