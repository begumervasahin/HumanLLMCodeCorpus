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
tweets['text'] = tweets_data.apply(lambda tweet: tweet['text'])
tweets['lang'] = tweets_data.apply(lambda tweet: tweet['lang'])
tweets['country'] = tweets_data.apply(lambda tweet: tweet['place']['country'] if tweet['place'] is not None else None)
tweets_by_lang = tweets['lang'].value_counts()
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Top 5 languages in tweets', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
tweets_by_country = tweets['country'].value_counts()
plt.show()
print("Visualization complete.")