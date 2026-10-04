import json
import pandas as pd
import matplotlib.pyplot as plt
b1 = '/home/nick/projects/twitter_data.txt'
b2 = []
with open(b1, "r") as tweets_file:
    for line in tweets_file:
        try:
            b3 = json.loads(line)
            b2.append(b3)
        except json.JSONDecodeError:
            continue
print(f"Number of b4 loaded: {len(b2)}")
b4 = pd.DataFrame(b2)
b4['text'] = b2.apply(lambda b3: b3['text'])
b4['lang'] = b2.apply(lambda b3: b3['lang'])
b4['country'] = b2.apply(lambda b3: b3['place']['country'] if b3['place'] is not None else None)
b5 = b4['lang'].value_counts()
fig, b6 = plt.subplots()
b6.tick_params(b7 = 'x', labelsize=15)
b6.tick_params(b7 = 'y', labelsize=10)
b6.set_xlabel('Languages', b8 = 15)
b6.set_ylabel('Number of b4', b8 = 15)
b6.set_title('Top 5 languages in b4', b8 = 15, fontweight='bold')
b5[:5].plot(b6 = b6, kind='bar', color='red')
b9 = b4['country'].value_counts()
plt.show()
print("Visualization complete.")