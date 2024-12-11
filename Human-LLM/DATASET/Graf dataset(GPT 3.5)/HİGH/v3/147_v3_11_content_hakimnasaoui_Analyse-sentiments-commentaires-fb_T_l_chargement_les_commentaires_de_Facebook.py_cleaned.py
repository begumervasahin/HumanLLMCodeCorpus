import requests
import pandas as pd
import os
import sys
def fonk1(b7, b8, b9):
    b1 = []
    b2 = []
    b3 = f"https:
    while True:
        b4 = requests.get(b3)
        b5 = b4.json()
        for comment_data in b5['b5']:
            b1.append(comment_data.get('message').encode('utf-8').strip())
            b2.append(comment_data.get('created_time'))
        b6 = b5.get('paging', {}).get('next')
        if not b6:
            break
        b3 = b6
    return b1, b2
def fonk2():
    b7 = os.environ.get('FB_TOKEN')
    if not b7:
        print("Please provide the Facebook token as an environment variable (FB_TOKEN)")
        sys.exit(-1)
    b8 = "624258451196"
    b9 = "12488754962145785"
    b1, b2 = fonk1(b7, b8, b9)
    b10 = pd.DataFrame({'comment': b1, 'date': b2})
    b10['date'] = pd.to_datetime(b10['date'])
    b10['day_of_week'] = b10['date'].dt.day_name()
    b10['year'] = b10['date'].dt.year
    b10['month'] = b10['date'].dt.month
    b10['count'] = 1
    print("\nGenerating JSON file...")
    b10.to_json('comment_data.json')
    print("JSON file generated successfully.")
if b11 = = "__main__":
    fonk2()