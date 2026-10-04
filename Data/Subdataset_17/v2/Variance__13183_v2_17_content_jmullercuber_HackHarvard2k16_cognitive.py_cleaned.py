import json
import time
import requests
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
def documents_to_sentiments(docs):
    request_body = {
        'documents': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(docs) if doc
        ]
    }
    response = requests.post(
        'https:
        headers=headers,
        data=json.dumps(request_body)
    )
    result = {
        'body': request_body,
        'result': response.json()
    }
    return result
def documents_to_topics(docs):
    request_body = {
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
        data=json.dumps(request_body)
    )
    operation_location = response.headers['operation-location']
    operation_path = operation_location[operation_location.index('.com') + 4:]
    result = {'body': request_body}
    while True:
        time.sleep(5)
        status_response = requests.get(
            'https:
            headers=headers
        )
        status_data = status_response.json()
        if 'status' in status_data and status_data['status'] == 'Succeeded':
            result['result'] = status_data
            break
    return result
documents = ["This is a sample document.", "Another document here.", ""]
print(documents_to_sentiments(documents))
print(documents_to_topics(documents))