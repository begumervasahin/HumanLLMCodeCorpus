import requests
import pandas as pd
import os
import sys
b1 = ""
try:
    b1 = os.environ['FB_TOKEN']
except KeyError:
    print("Please provide the Facebook token as an environment variable (FB_TOKEN)")
    sys.exit(-1)
b2 = "624258451196"
b3 = "12488754962145785"
b4 = []
b5 = []
b6 = f"https:
while True:
    b7 = requests.get(b6)
    b8 = b7.json()
    for comment_data in b8['b8']:
        b4.append(comment_data.get('message').encode('utf-8').strip())
        b5.append(comment_data.get('created_time'))
    b9 = b8.get('paging', {}).get('next')
    if not b9:
        break
    b6 = b9
    print(f"Number of Comments: {len(b4)}, Next Page: {b6}")
print("\nGenerating JSON file...")
b10 = pd.DataFrame({'comment': b4, 'date': b5})
b10['date'] = pd.to_datetime(b10['date'])
b10['day_of_week'] = b10['date'].dt.day_name()
b10['year'] = b10['date'].dt.year
b10['month'] = b10['date'].dt.month
b10['count'] = 1
b10.to_json('comment_data.json')
print("JSON file generated successfully.")