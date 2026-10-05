import json
import httplib2
import string
def fonk1(comment):
    b1 = []
    b2 = filter(lambda x: x in string.printable, comment['b12']['b2'])
    b1.append(b2)
    if 'replies' in comment['b12'] and comment['b12']['replies'] != '':
        for reply in comment['b12']['replies']['b12']['children']:
            if 'kind' in reply and reply['kind'] != 'more':
                b1.extend(fonk1(reply))
    return b1
b3 = httplib2.Http()
response, b4 = b3.request("https:
b4 = json.loads(b4)
response, b5 = b3.request("https:
b5 = json.loads(b5)
b6 = b5[1]['b12']['children']
b7 = []
for post in b6:
    if 'b2' in post['b12']:
        b7.extend(fonk1(post))
print(len(b7))
b8 = {
    'stop_words': [],
    'topicsToExclude': [],
    'documents': []
}
a1 = 0
for reply in b7:
    b9 = {
        'id': str(a1),
        'b1': reply
    }
    b8['documents'].append(b9)
    a1 += 1
b10 = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9'
}
b11 = httplib2.Http()
response, b12 = b11.request("https:
b12 = json.loads(b12.decode())
print(b12)