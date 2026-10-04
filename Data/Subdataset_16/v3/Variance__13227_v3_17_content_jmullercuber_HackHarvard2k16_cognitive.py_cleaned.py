import json
import time
import requests
b1 = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
def fonk1(b12):
    return {
        'b12': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(b12) if doc
        ]
    }
def fonk2(b12):
    b2 = fonk4(b12)
    b3 = requests.post(
        'https:
        b4 = b1,
        b5 = json.dumps(b2)
    )
    return {
        'body': b2,
        'b8': b3.json()
    }
def fonk3(b12):
    b2 = {
        'stopWords': [],
        'topicsToExclude': [],
        'b12': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(b12)
        ]
    }
    b3 = requests.post(
        'https:
        b4 = b1,
        b5 = json.dumps(b2)
    )
    b6 = b3.b4['operation-location']
    b7 = b6[b6.index('.com') + 4:]
    b8 = {'body': b2}
    while True:
        time.sleep(5)
        b9 = requests.get(
            'https:
            b4 = b1
        )
        b10 = b9.json()
        if b10.get('status') == 'Succeeded':
            b8['b8'] = b10
            break
    return b8
if b11 = = "__main__":
    b12 = ["This is a sample document.", "Another document here.", ""]
    print(fonk5(b12))
    print(fonk6(b12))
import json
import time
import requests
b1 = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
def fonk4(b12):
    return {
        'b12': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(b12) if doc
        ]
    }
def fonk5(b12):
    b2 = fonk4(b12)
    b3 = requests.post(
        'https:
        b4 = b1,
        b5 = json.dumps(b2)
    )
    return {
        'body': b2,
        'b8': b3.json()
    }
def fonk6(b12):
    b2 = {
        'stopWords': [],
        'topicsToExclude': [],
        'b12': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(b12)
        ]
    }
    b3 = requests.post(
        'https:
        b4 = b1,
        b5 = json.dumps(b2)
    )
    b6 = b3.b4['operation-location']
    b7 = b6[b6.index('.com') + 4:]
    b8 = {'body': b2}
    while True:
        time.sleep(5)
        b9 = requests.get(
            'https:
            b4 = b1
        )
        b10 = b9.json()
        if b10.get('status') == 'Succeeded':
            b8['b8'] = b10
            break
    return b8
if b11 = = "__main__":
    b12 = ["This is a sample document.", "Another document here.", ""]
    print(fonk5(b12))
    print(fonk6(b12))