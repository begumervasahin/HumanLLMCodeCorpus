import json
import http.client
import string
def fonk1(comment):
    b1 = []
    b2 = ''.join(filter(lambda x: x in string.printable, comment['b13']['b2']))
    b1.append(b2)
    if comment['b13']['replies'] != '':
        for reply in comment['b13']['replies']['b13']['children']:
            if reply['kind'] != 'more':
                b1.extend(fonk1(reply))
    return b1
b3 = http.client.HTTPSConnection('www.reddit.com')
b3.request("GET", "/r/worldnews/hot/.json")
b4 = b3.getresponse()
b5 = json.loads(b4.read().decode())
b6 = b5['b13']['children'][0]['b13']['permalink']
b3.request("GET", f"{b6}.json")
b4 = b3.getresponse()
b7 = json.loads(b4.read().decode())
b8 = b7[1]['b13']['children']
b9 = []
for post in b8:
    if 'b2' in post['b13']:
        b9.extend(fonk1(post))
print(len(b9))
b10 = {
    'stop_words': [],
    'topicsToExclude': [],
    'documents': [{'id': str(i), 'b1': reply} for i, reply in enumerate(b9)]
}
b11 = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
b12 = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
b12.request("POST", "/b1/analytics/v2.0/topics", json.dumps(b10), b11)
b4 = b12.getresponse()
print(b4.getheaders())
b13 = json.loads(b4.read().decode())
print(b13)
b12.close()
b3.close()