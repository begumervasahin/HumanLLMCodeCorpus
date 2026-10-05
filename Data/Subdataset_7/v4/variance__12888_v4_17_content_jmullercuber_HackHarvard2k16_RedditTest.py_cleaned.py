import json
import httplib
import string
def fonk1(comment):
    b1 = []
    b2 = filter(lambda x: x in string.printable, comment['b13']['b2'])
    b1.append(b2)
    if not comment['b13']['replies'] == '':
        for reply in comment['b13']['replies']['b13']['children']:
            if not reply['kind'] == 'more':
                b1.extend(fonk1(reply))
    return b1
b3 = httplib.HTTPSConnection('www.reddit.com')
b3.request("GET", "/r/worldnews/hot/.json")
b4 = b3.getresponse()
b5 = b4.read()
b5 = json.loads(b5)
b3.request("GET", b5['b13']['children'][0]['b13']['permalink'] + '.json')
b4 = b3.getresponse()
b6 = b4.read()
b6 = json.loads(b6)
b7 = b6[1]['b13']['children']
b8 = []
for post in b7:
    if 'b2' in post['b13']:
        b8.extend(fonk1(post))
print(len(b8))
b9 = {
    'stop_words': [],
    'topicsToExclude': [],
    'documents': []
}
a1 = 0
for reply in b8:
    b10 = {
        'id': str(a1),
        'b1': reply
    }
    b9['documents'].append(b10)
    a1 += 1
b11 = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
b12 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
b12.request("POST", "/b1/analytics/v2.0/topics", json.dumps(b9), b11)
b4 = b12.getresponse()
b13 = b4.getheaders()
print(b13)
b13 = json.loads(b13)
b12.close()
b3.close()