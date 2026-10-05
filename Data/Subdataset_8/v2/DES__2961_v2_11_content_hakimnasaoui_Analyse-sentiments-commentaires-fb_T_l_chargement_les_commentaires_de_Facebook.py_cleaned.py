import requests
import pandas as pd
import os
import sys
fb_token = ""
try:
    fb_token = os.environ['FB_TOKEN']
except KeyError:
    print("Please provide the Facebook token as an environment variable (FB_TOKEN)")
    sys.exit(-1)
fb_page_id = "624258451196"
fb_post_id = "12488754962145785"
comments = []
dates = []
url = f"https:
while True:
    response = requests.get(url)
    data = response.json()
    for comment_data in data['data']:
        comments.append(comment_data.get('message').encode('utf-8').strip())
        dates.append(comment_data.get('created_time'))
    next_page = data.get('paging', {}).get('next')
    if not next_page:
        break
    url = next_page
    print(f"Number of Comments: {len(comments)}, Next Page: {url}")
print("\nGenerating JSON file...")
df = pd.DataFrame({'comment': comments, 'date': dates})
df['date'] = pd.to_datetime(df['date'])
df['day_of_week'] = df['date'].dt.day_name()
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['count'] = 1
df.to_json('comment_data.json')
print("JSON file generated successfully.")