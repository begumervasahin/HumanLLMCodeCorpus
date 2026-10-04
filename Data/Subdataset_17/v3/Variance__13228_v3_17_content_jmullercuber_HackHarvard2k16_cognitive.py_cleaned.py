import json
import time
import requests
HEADERS = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
def prepare_request_body(documents):
    return {
        'documents': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(documents) if doc
        ]
    }
def documents_to_sentiments(documents):
    request_body = prepare_request_body(documents)
    response = requests.post(
        'https:
        headers=HEADERS,
        data=json.dumps(request_body)
    )
    return {
        'body': request_body,
        'result': response.json()
    }
def documents_to_topics(documents):
    request_body = {
        'stopWords': [],
        'topicsToExclude': [],
        'documents': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(documents)
        ]
    }
    response = requests.post(
        'https:
        headers=HEADERS,
        data=json.dumps(request_body)
    )
    operation_location = response.headers['operation-location']
    operation_path = operation_location[operation_location.index('.com') + 4:]
    result = {'body': request_body}
    while True:
        time.sleep(5)
        status_response = requests.get(
            'https:
            headers=HEADERS
        )
        status_data = status_response.json()
        if status_data.get('status') == 'Succeeded':
            result['result'] = status_data
            break
    return result
if __name__ == "__main__":
    documents = ["This is a sample document.", "Another document here.", ""]
    print(documents_to_sentiments(documents))
    print(documents_to_topics(documents))
import json
import time
import requests
HEADERS = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
def prepare_request_body(documents):
    return {
        'documents': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(documents) if doc
        ]
    }
def documents_to_sentiments(documents):
    request_body = prepare_request_body(documents)
    response = requests.post(
        'https:
        headers=HEADERS,
        data=json.dumps(request_body)
    )
    return {
        'body': request_body,
        'result': response.json()
    }
def documents_to_topics(documents):
    request_body = {
        'stopWords': [],
        'topicsToExclude': [],
        'documents': [
            {'id': str(i), 'text': doc}
            for i, doc in enumerate(documents)
        ]
    }
    response = requests.post(
        'https:
        headers=HEADERS,
        data=json.dumps(request_body)
    )
    operation_location = response.headers['operation-location']
    operation_path = operation_location[operation_location.index('.com') + 4:]
    result = {'body': request_body}
    while True:
        time.sleep(5)
        status_response = requests.get(
            'https:
            headers=HEADERS
        )
        status_data = status_response.json()
        if status_data.get('status') == 'Succeeded':
            result['result'] = status_data
            break
    return result
if __name__ == "__main__":
    documents = ["This is a sample document.", "Another document here.", ""]
    print(documents_to_sentiments(documents))
    print(documents_to_topics(documents))