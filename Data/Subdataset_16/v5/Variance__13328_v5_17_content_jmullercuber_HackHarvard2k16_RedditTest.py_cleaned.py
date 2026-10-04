import json
import http.client
import string
def fonk1(text):
    return ''.join(filter(lambda x: x in string.printable, text))
def fonk2(comment):
    b1 = []
    b2 = fonk1(comment['data']['b2'])
    b1.append(b2)
    if comment['data']['replies']:
        for reply in comment['data']['replies']['data']['children']:
            if reply['kind'] != 'more':
                b1.extend(fonk2(reply))
    return b1
def fonk3(connection, url):
    connection.request("GET", url)
    b3 = connection.getresponse()
    return json.loads(b3.read())
def fonk4(b9):
    b4 = b9[1]['data']['children']
    b5 = []
    for post in b4:
        if 'b2' in post['data']:
            b5.extend(fonk2(post))
    return b5
def fonk5(comments):
    return {
        'stop_words': [],
        'topicsToExclude': [],
        'documents': [{'id': str(i), 'text': comment} for i, comment in enumerate(comments)]
    }
def fonk6():
    b6 = http.client.HTTPSConnection('www.reddit.com')
    b7 = fonk3(b6, "/r/worldnews/hot/.json")
    b8 = b7['data']['children'][0]['data']['permalink']
    b9 = fonk3(b6, f"{b8}.json")
    b5 = fonk4(b9)
    print(f"Total comments extracted: {len(b5)}")
    b10 = fonk5(b5)
    b11 = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
    }
    b12 = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    b12.request("POST", "/text/analytics/v2.0/topics", json.dumps(b10), b11)
    b3 = b12.getresponse()
    b13 = b3.getheaders()
    b14 = json.loads(b3.read())
    print(b13)
    print(b14)
    b12.close()
    b6.close()
if b15 = = "__main__":
    fonk6()