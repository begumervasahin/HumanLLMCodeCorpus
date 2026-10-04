import pandas as pd
import re
from datetime import datetime
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud
import seaborn as sns
import numpy as np
from PIL import Image
news = pd.read_csv('news.csv')
news = news[(news['Year'] >= 2011) & (news['Year'] <= 2019)]
news['Date'] = news['Year'].astype(str) + ' ' + news['Month'] + ' ' + news['Day'].astype(str)
news['Date'] = news['Date'].apply(lambda x: datetime.strptime(x, '%Y %b %d').date())
def check_any(pattern1, pattern2, string):
    string = string.lower()
    if re.search(pattern1, string) is not None and re.search(pattern2, string) is not None:
        return 1
    else:
        return 0
news['Article_bank_purdue'] = news['Article'].apply(lambda x: check_any('purdue', 'bankruptcy', x))
print(news['Article_bank_purdue'].sum())
for i in ['Header', 'Article']:
    for y in ['opioid', 'purdue', 'bankruptcy']:
        news[i + '_' + y] = news[i].apply(lambda x: check_any(y, '', x))
        print(news[i + '_' + y].sum())
news['Date'] = pd.to_datetime(news['Date'])
news = news.set_index('Date')
news = news['2011-09-26':'2019-09-14']
news = news.drop(['Unnamed: 0'], axis=1)
df_grouped = news.groupby(news.index.year).agg({'Article_opioid': 'sum', 'Article_purdue': 'sum', 'Article_bank_purdue': 'sum'})
print(df_grouped)
df_corr = df_grouped.corr(method="pearson")
print(df_corr)
sns.set(rc={'figure.figsize': (11, 4)})
ax = news.groupby(news.index.year).agg({'Article_opioid': 'sum', 'Article_purdue': 'sum', 'Article_bank_purdue': 'sum'}).plot(marker='o', linestyle='-')
ax.set_ylabel('Number of Articles')
ax.set_title('Number of Articles per Year Containing Certain Words')
plt.savefig('Trend_words.png', bbox_inches='tight')
stop = stopwords.words('english')
stop.extend(['one', 'told cnn', 'trump', 'president', 'say', 'said', 'may', 'new', 'according', 'many', 'two',
             'make', 'made', 'including', 'work', 'need', 'know', 'year', 'still', 'want', 'take', 'going',
             'state', 'monday', 'first', 'week', 'pr', 'michael', 'jackson', 'donald'])
mask = np.array(Image.open("usa_map.jpg"))
wc = WordCloud(background_color="black", max_words=2000, width=800, height=400, mask=mask)
for_cloud = " ".join(news.loc[news.Article_opioid == 1]['Article'].apply(lambda text: " ".join(word for word in text.lower().split() if word not in stop)))
wc.generate(for_cloud)
wc.to_file("cloud_opioid.png")
news.to_csv('news_final.csv')