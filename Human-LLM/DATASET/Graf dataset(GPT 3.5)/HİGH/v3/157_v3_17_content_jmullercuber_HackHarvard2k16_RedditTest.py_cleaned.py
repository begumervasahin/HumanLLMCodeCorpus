import json
import httplib2
import string
def fonk1(text):
    b1 = string.printable
    return filter(lambda x: x in b1, text)
def fonk2(comment):
    b2 = []
    if 'body' in comment['data']:
        b2.append(fonk1(comment['data']['body']))
    if 'replies' in comment['data'] and comment['data']['replies'] != '':
        for reply in comment['data']['replies']['data']['children']:
            if 'kind' in reply and reply['kind'] != 'more':
                b2.extend(fonk2(reply))
    return b2
b3 = httplib2.Http()
response, b4 = b3.request("https:
b4 = json.loads(b4)
response, b5 = b3.request("https:
b5 = json.loads(b5)
b6 = b5[1]['data']['children']
b7 = []
for post in b6:
    b7.extend(fonk2(post))
print("Total b2 processed:", len(b7))
b8 = {
    'stop_words': [],
    'topicsToExclude': [],
    'documents': []
}
for idx, comment in enumerate(b7):
    b8['documents'].append({'id': str(idx), 'text': comment})
b9 = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9'
}
response, b10 = b3.request("https:
b10 = json.loads(b10.decode())
print("Analysis results:", b10)