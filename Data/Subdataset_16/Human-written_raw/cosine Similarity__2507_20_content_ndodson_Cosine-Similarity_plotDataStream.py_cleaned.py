import json
import pandas as pd
import matplotlib.pyplot as plt
b1 = '/home/nick/projects/twitter_data.txt'
b2 = []
b3 = open(b1, "r")
for line in b3:
    try:
        b4 = json.loads(line)
        b2.append(b4)
    except:
        continue
print len(b2)
b5 = pd.DataFrame()
b5['text'] = map(lambda b4: b4['text'], b2)
b5['lang'] = map(lambda b4: b4['lang'], b2)
b5['country'] = map(lambda b4: b4['place']['country'] if b4['place'] != None else None, b2)
b6 = b5['lang'].value_counts()
fig, b7 = plt.subplots()
b7.tick_params(b8 = 'x', labelsize=15)
b7.tick_params(b8 = 'y', labelsize=10)
b7.set_xlabel('Languages', b9 = 15)
b7.set_ylabel('Number of b5' , b9 = 15)
b7.set_title('Top 5 languages', b9 = 15, fontweight='bold')
b6[:5].plot(b7 = b7, kind='bar', color='red')
b10 = b5['country'].value_counts()
plt.show()
print "we done"