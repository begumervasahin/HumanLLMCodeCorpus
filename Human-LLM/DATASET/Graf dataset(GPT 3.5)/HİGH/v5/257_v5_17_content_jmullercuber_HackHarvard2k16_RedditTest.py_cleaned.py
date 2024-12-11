import json
import httplib
import string
def fonk1(comment):
    b1 = []
    b2 = filter(lambda x: x in string.printable, comment['b5']['b2'])
    b1.append(b2)
    if 'replies' in comment['b5'] and comment['b5']['replies'] != '':
        for reply in comment['b5']['replies']['b5']['children']:
            if reply['kind'] != 'more':
                b1.extend(fonk1(reply))
    return b1
def fonk2(url):
    b3 = httplib.HTTPSConnection('www.reddit.com')
    b3.request("GET", url)
    b4 = b3.getresponse()
    b5 = b4.read()
    b3.close()
    return json.loads(b5)
b6 = fonk2("/r/worldnews/hot/.json")
b7 = b6['b5']['children'][0]['b5']['permalink']
b8 = fonk2(b7 + '.json')
b9 = b8[1]['b5']['children']
b10 = []
for post in b9:
    if 'b2' in post['b5']:
        b10.extend(fonk1(post))
print("Total Comments:", len(b10))
b11 = []
for idx, comment in enumerate(b10):
    b11.append({'id': str(idx), 'text': comment})
b12 = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
b13 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
b13.request("POST", "/text/analytics/v2.0/topics", json.dumps({'b11': b11}), b12)
b4 = b13.getresponse()
b5 = b4.read()
print("API Response:", b5)
b13.close()