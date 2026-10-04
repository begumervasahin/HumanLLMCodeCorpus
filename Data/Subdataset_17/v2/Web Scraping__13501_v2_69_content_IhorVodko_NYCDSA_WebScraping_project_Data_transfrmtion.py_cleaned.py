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
def check_keyword(column, keyword):
    return column.apply(lambda x: 1 if re.search(keyword, x.lower()) else 0)
for column in ['Header', 'Article']:
    for keyword in ['opioid', 'purdue', 'bankruptcy']:
        news[f'{column}_{keyword}'] = check_keyword(news[column], keyword)
        print(news[f'{column}_{keyword}'].sum())
news['Date'] = pd.to_datetime(news['Date'])
news = news.set_index('Date')
news = news['2011-09-26':'2019-09-14']
news = news.drop(columns=['Unnamed: 0'])
df_grouped = news.groupby(news.index.year).agg({
    'Article_opioid': 'sum',
    'Article_purdue': 'sum',
    'Article_bank_purdue': 'sum'
})
print(df_grouped)
df_corr = df_grouped.corr(method="pearson")
print(df_corr)
sns.set(rc={'figure.figsize': (11, 4)})
ax = df_grouped.plot(marker='o', linestyle='-')
ax.set_ylabel('Number of Articles')
ax.set_title('Number of Articles per Year Containing Certain Words')
plt.savefig('Trend_words.png', bbox_inches='tight')
stop_words = set(stopwords.words('english')).union(set([
    'one', 'told cnn', 'trump', 'president', 'say', 'said', 'may', 'new', 'according', 'many', 'two',
    'make', 'made', 'including', 'work', 'need', 'know', 'year', 'still', 'want', 'take', 'going',
    'state', 'monday', 'first', 'week', 'pr', 'michael', 'jackson', 'donald'
]))
mask = np.array(Image.open("usa_map.jpg"))
wc = WordCloud(background_color="black", max_words=2000, width=800, height=400, mask=mask)
articles_with_opioid = news.loc[news.Article_opioid == 1]['Article']
for_cloud = " ".join(
    word for text in articles_with_opioid
    for word in text.lower().split()
    if word not in stop_words
)
wc.generate(for_cloud)
wc.to_file("cloud_opioid.png")
news.to_csv('news_final.csv')