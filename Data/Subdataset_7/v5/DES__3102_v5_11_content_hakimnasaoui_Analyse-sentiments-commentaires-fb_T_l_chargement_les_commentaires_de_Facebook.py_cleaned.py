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
    b7 = os.environ.get('FB_TOKEN', '')
    if not b7:
        print("Please provide the Facebook token as an environment variable (FB_TOKEN)")
        sys.exit(-1)
    b8 = "624258451196"
    b9 = "12488754962145785"
    comments, b10 = fonk1(b7, b8, b9)
    b11 = pd.DataFrame({'comment': comments, 'date': b10})
    b11['date'] = pd.to_datetime(b11['date'])
    b11['day_of_week'] = b11['date'].dt.day_name()
    b11['year'] = b11['date'].dt.year
    b11['month'] = b11['date'].dt.month
    b11['count'] = 1
    print("\nGenerating JSON file...")
    b11.to_json('commentaires_data.json')
    print("JSON file generated successfully.")
if b12 = = "__main__":
    fonk2()