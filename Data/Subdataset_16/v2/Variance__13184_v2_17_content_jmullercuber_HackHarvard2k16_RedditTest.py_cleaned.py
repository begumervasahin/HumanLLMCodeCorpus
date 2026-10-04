import json
import http.client
import string
def fonk1(comment):
    b1 = []
    b2 = ''.join(filter(lambda x: x in string.printable, comment['b5']['b2']))
    b1.append(b2)
    if comment['b5']['replies'] != '':
        for reply in comment['b5']['replies']['b5']['children']:
            if reply['kind'] != 'more':
                b1.extend(fonk1(reply))
    return b1
def fonk2(b8):
    b3 = http.client.HTTPSConnection('www.reddit.com')
    b3.request("GET", f"/r/{b8}/hot/.json")
    b4 = b3.getresponse()
    b5 = json.loads(b4.read().decode())
    b3.close()
    return b5
def fonk3(permalink):
    b3 = http.client.HTTPSConnection('www.reddit.com')
    b3.request("GET", f"{permalink}.json")
    b4 = b3.getresponse()
    b5 = json.loads(b4.read().decode())
    b3.close()
    return b5
def fonk4(comments):
    b6 = [{'id': str(i), 'b1': comment} for i, comment in enumerate(comments)]
    return {
        'stop_words': [],
        'topicsToExclude': [],
        'b6': b6
    }
def fonk5(b9, b15):
    b7 = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': b9,
    }
    b3 = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    b3.request("POST", "/b1/analytics/v2.0/topics", json.dumps(b15), b7)
    b4 = b3.getresponse()
    b5 = json.loads(b4.read().decode())
    b3.close()
    return b5
def fonk6():
    b8 = "worldnews"
    b9 = 'b3f5d9f8d81046598dedc07a7541e2c9'
    b10 = fonk2(b8)
    b11 = b10['b5']['children'][0]['b5']['permalink']
    b12 = fonk3(b11)
    b13 = b12[1]['b5']['children']
    b14 = []
    for post in b13:
        if 'b2' in post['b5']:
            b14.extend(fonk1(post))
    print(f"Total comments collected: {len(b14)}")
    b15 = fonk4(b14)
    b16 = fonk5(b9, b15)
    print(json.dumps(b16, b17 = 4))
if b18 = = "__main__":
    fonk6()