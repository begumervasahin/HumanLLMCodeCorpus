import json
import time
import requests
b1 = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
def fonk1(docs):
    b2 = {
        'b10': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(docs) if doc
        ]
    }
    b3 = requests.post(
        'https:
        b1 = b1,
        b4 = json.dumps(b2)
    )
    b5 = {
        'body': b2,
        'b5': b3.json()
    }
    return b5
def fonk2(docs):
    b2 = {
        'stopWords': [],
        'topicsToExclude': [],
        'b10': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(docs)
        ]
    }
    b3 = requests.post(
        'https:
        b1 = b1,
        b4 = json.dumps(b2)
    )
    b6 = b3.b1['operation-location']
    b7 = b6[b6.index('.com') + 4:]
    b5 = {'body': b2}
    while True:
        time.sleep(5)
        b8 = requests.get(
            'https:
            b1 = b1
        )
        b9 = b8.json()
        if 'status' in b9 and b9['status'] == 'Succeeded':
            b5['b5'] = b9
            break
    return b5
b10 = ["This is a sample document.", "Another document here.", ""]
print(fonk1(b10))
print(fonk2(b10))