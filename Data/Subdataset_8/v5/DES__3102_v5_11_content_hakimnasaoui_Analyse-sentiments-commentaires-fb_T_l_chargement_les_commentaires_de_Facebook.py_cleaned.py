import requests
import pandas as pd
import os
import sys
def fetch_comments(fb_token, fb_page_id, fb_post_id):
    comment_list = []
    date_list = []
    url = f"https:
    while True:
        response = requests.get(url)
        data = response.json()
        for comment_data in data['data']:
            comment_list.append(comment_data.get('message').encode('utf-8').strip())
            date_list.append(comment_data.get('created_time'))
        next_page = data.get('paging', {}).get('next')
        if not next_page:
            break
        url = next_page
    return comment_list, date_list
def main():
    fb_token = os.environ.get('FB_TOKEN', '')
    if not fb_token:
        print("Please provide the Facebook token as an environment variable (FB_TOKEN)")
        sys.exit(-1)
    fb_page_id = "624258451196"
    fb_post_id = "12488754962145785"
    comments, dates = fetch_comments(fb_token, fb_page_id, fb_post_id)
    df = pd.DataFrame({'comment': comments, 'date': dates})
    df['date'] = pd.to_datetime(df['date'])
    df['day_of_week'] = df['date'].dt.day_name()
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['count'] = 1
    print("\nGenerating JSON file...")
    df.to_json('commentaires_data.json')
    print("JSON file generated successfully.")
if __name__ == "__main__":
    main()