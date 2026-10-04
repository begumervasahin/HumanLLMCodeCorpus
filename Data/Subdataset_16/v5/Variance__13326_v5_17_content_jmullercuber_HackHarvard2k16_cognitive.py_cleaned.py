import json
import httplib
import time
b1 = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
def fonk1(docs):
    b2 = {
        'documents': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(docs) if doc
        ]
    }
    b3 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    b3.request("POST", "/text/analytics/v2.0/sentiment", json.dumps(b2), b1)
    b4 = b3.getresponse()
    b5 = b4.read()
    b3.close()
    b6 = json.loads(b5)
    return {'body': b2, 'b6': b6}
def fonk2(docs):
    b2 = {
        'stop_words': [],
        'topicsToExclude': [],
        'documents': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(docs)
        ]
    }
    b3 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    b3.request("POST", "/text/analytics/v2.0/topics", json.dumps(b2), b1)
    b4 = b3.getresponse()
    b7 = b4.getheader('operation-location')
    print(b4.getheaders())
    print(b7)
    if '.com' in b7:
        b7 = b7[b7.index('.com') + 4:]
    print(b7)
    b8 = {'body': b2}
    while True:
        time.sleep(5)
        b9 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        b9.request("GET", b7, '', b1)
        b4 = b9.getresponse()
        b5 = b4.read()
        b5 = json.loads(b5)
        if b5.get('status') == 'Succeeded':
            b8['b6'] = b5
            break
        b9.close()
    b3.close()
    return b8