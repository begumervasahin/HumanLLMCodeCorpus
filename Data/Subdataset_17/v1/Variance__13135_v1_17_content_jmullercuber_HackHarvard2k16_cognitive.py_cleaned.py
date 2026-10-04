import json
import time
import requests
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
def documents_to_sentiments(docs):
    c_body = {
        'documents': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(docs) if doc
        ]
    }
    response = requests.post(
        'https:
        headers=headers,
        data=json.dumps(c_body)
    )
    res = {
        'body': c_body,
        'result': response.json()
    }
    return res
def documents_to_topics(docs):
    c_body = {
        'stopWords': [],
        'topicsToExclude': [],
        'documents': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(docs)
        ]
    }
    response = requests.post(
        'https:
        headers=headers,
        data=json.dumps(c_body)
    )
    op_loc = response.headers['operation-location']
    op_loc_path = op_loc[op_loc.index('.com') + 4:]
    res = {'body': c_body}
    while True:
        time.sleep(5)
        status_response = requests.get(
            'https:
            headers=headers
        )
        data = status_response.json()
        if 'status' in data and data['status'] == 'Succeeded':
            res['result'] = data
            break
    return res
docs = ["This is a sample document.", "Another document here.", ""]
print(documents_to_sentiments(docs))
print(documents_to_topics(docs))