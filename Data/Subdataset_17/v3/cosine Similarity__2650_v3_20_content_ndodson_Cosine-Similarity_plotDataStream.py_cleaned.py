import json
import pandas as pd
import matplotlib.pyplot as plt
tweets_data_path = '/home/nick/projects/twitter_data.txt'
tweets_data = []
with open(tweets_data_path, "r") as tweets_file:
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except json.JSONDecodeError:
            continue
print(f"Number of tweets loaded: {len(tweets_data)}")
tweets = pd.DataFrame(tweets_data)
tweets['text'] = tweets['text']
tweets['lang'] = tweets['lang']
tweets['country'] = tweets['place'].apply(lambda place: place['country'] if place is not None else None)
tweets_by_lang = tweets['lang'].value_counts()
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of Tweets', fontsize=15)
ax.set_title('Top 5 Languages in Tweets', fontsize=18, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='skyblue')
plt.tight_layout()
plt.show()
print("Visualization complete.")