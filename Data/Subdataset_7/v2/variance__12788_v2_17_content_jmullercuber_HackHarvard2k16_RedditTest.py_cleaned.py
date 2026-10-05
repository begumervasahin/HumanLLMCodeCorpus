import json
import httplib2
import string
def fonk1(comment):
    b1 = string.printable
    b2 = []
    b3 = filter(lambda x: x in b1, comment['data']['b3'])
    b2.append(b3)
    if 'replies' in comment['data'] and comment['data']['replies'] != '':
        for reply in comment['data']['replies']['data']['children']:
            if 'kind' in reply and reply['kind'] != 'more':
                b2.extend(fonk1(reply))
    return b2
b4 = httplib2.Http()
response, b5 = b4.request("https:
b5 = json.loads(b5)
response, b6 = b4.request("https:
b6 = json.loads(b6)
b7 = b6[1]['data']['children']
b8 = []
for post in b7:
    if 'b3' in post['data']:
        b8.extend(fonk1(post))
print("Total comments processed:", len(b8))
b9 = {
    'stop_words': [],
    'topicsToExclude': [],
    'documents': []
}
a1 = 0
for comment in b8:
    b10 = {
        'id': str(a1),
        'b2': comment
    }
    b9['documents'].append(b10)
    a1 += 1
b11 = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9'
}
response, b12 = b4.request("https:
b12 = json.loads(b12.decode())
print("Analysis results:", b12)