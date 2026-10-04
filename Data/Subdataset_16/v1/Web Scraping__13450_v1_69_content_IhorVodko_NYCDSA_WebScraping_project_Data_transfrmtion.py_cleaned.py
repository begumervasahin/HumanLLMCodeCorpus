import pandas as pd
import re
from datetime import datetime
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud
import seaborn as sns
import numpy as np
from PIL import Image
b1 = pd.read_csv('b1.csv')
b1 = b1[(b1['Year'] >= 2011) & (b1['Year'] <= 2019)]
b1['Date'] = b1['Year'].astype(str) + ' ' + b1['Month'] + ' ' + b1['Day'].astype(str)
b1['Date'] = b1['Date'].apply(lambda x: datetime.strptime(x, '%Y %b %d').date())
def fonk1(pattern1, pattern2, b2):
    b2 = b2.lower()
    if re.search(pattern1, b2) is not None and re.search(pattern2, b2) is not None:
        return 1
    else:
        return 0
b1['Article_bank_purdue'] = b1['Article'].apply(lambda x: fonk1('purdue', 'bankruptcy', x))
print(b1['Article_bank_purdue'].sum())
for i in ['Header', 'Article']:
    for y in ['opioid', 'purdue', 'bankruptcy']:
        b1[i + '_' + y] = b1[i].apply(lambda x: fonk1(y, '', x))
        print(b1[i + '_' + y].sum())
b1['Date'] = pd.to_datetime(b1['Date'])
b1 = b1.set_index('Date')
b1 = b1['2011-09-26':'2019-09-14']
b1 = b1.drop(['Unnamed: 0'], axis=1)
b3 = b1.groupby(b1.index.year).agg({'Article_opioid': 'sum', 'Article_purdue': 'sum', 'Article_bank_purdue': 'sum'})
print(b3)
b4 = b3.corr(method="pearson")
print(b4)
sns.set(b5 = {'figure.figsize': (11, 4)})
b6 = b1.groupby(b1.index.year).agg({'Article_opioid': 'sum', 'Article_purdue': 'sum', 'Article_bank_purdue': 'sum'}).plot(marker='o', linestyle='-')
b6.set_ylabel('Number of Articles')
b6.set_title('Number of Articles per Year Containing Certain Words')
plt.savefig('Trend_words.png', b7 = 'tight')
b8 = stopwords.words('english')
b8.extend(['one', 'told cnn', 'trump', 'president', 'say', 'said', 'may', 'new', 'according', 'many', 'two',
             'make', 'made', 'including', 'work', 'need', 'know', 'year', 'still', 'want', 'take', 'going',
             'state', 'monday', 'first', 'week', 'pr', 'michael', 'jackson', 'donald'])
b9 = np.array(Image.open("usa_map.jpg"))
b10 = WordCloud(background_color="black", max_words=2000, width=800, height=400, b9=b9)
b11 = " ".join(b1.loc[b1.Article_opioid == 1]['Article'].apply(lambda text: " ".join(word for word in text.lower().split() if word not in b8)))
b10.generate(b11)
b10.to_file("cloud_opioid.png")
b1.to_csv('news_final.csv')