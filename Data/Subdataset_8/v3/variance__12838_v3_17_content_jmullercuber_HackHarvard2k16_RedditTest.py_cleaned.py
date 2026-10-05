import json
import httplib2
import string
def get_printable_text(text):
    printable_characters = string.printable
    return filter(lambda x: x in printable_characters, text)
def get_comments(comment):
    comments = []
    if 'body' in comment['data']:
        comments.append(get_printable_text(comment['data']['body']))
    if 'replies' in comment['data'] and comment['data']['replies'] != '':
        for reply in comment['data']['replies']['data']['children']:
            if 'kind' in reply and reply['kind'] != 'more':
                comments.extend(get_comments(reply))
    return comments
http_client = httplib2.Http()
response, subreddit_data = http_client.request("https:
subreddit_data = json.loads(subreddit_data)
response, post_data = http_client.request("https:
post_data = json.loads(post_data)
timeline_posts = post_data[1]['data']['children']
all_comments = []
for post in timeline_posts:
    all_comments.extend(get_comments(post))
print("Total comments processed:", len(all_comments))
request_body = {
    'stop_words': [],
    'topicsToExclude': [],
    'documents': []
}
for idx, comment in enumerate(all_comments):
    request_body['documents'].append({'id': str(idx), 'text': comment})
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9'
}
response, analysis_results = http_client.request("https:
analysis_results = json.loads(analysis_results.decode())
print("Analysis results:", analysis_results)